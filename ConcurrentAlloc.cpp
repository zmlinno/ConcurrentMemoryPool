#include "ConcurrentAlloc.h"
//这个cpp文件也是为了项目后加的，关键时候也是可以删除的，自由的
extern "C" {
    void* ConcurrentAlloc(size_t size)
    {
        if (size > MAX_BYTES)
        {
            size_t alignSize = SizeClass::RoundUp(size);
            size_t kpage = alignSize >> PAGE_SHIFT;

            PageCache::GetInstance()->_pageMtx.lock();
            Span* span = PageCache::GetInstance()->NewSpan(kpage);
            span->_objSize = size;
            PageCache::GetInstance()->_pageMtx.unlock();

            void* ptr = (void*)(span->_pageId << PAGE_SHIFT);
            return ptr;
        }
        else
        {
            if (pTLSThreadCache == nullptr)
            {
                static ObjectPool<ThreadCache> tcPool;
                pTLSThreadCache = tcPool.New();
            }
            return pTLSThreadCache->Allocate(size);
        }
    }

    void ConcurrentFree(void* ptr)
    {
        Span* span = PageCache::GetInstance()->MapObjectToSpan(ptr);
        size_t size = span->_objSize;

        if (size > MAX_BYTES)
        {
            PageCache::GetInstance()->_pageMtx.lock();
            PageCache::GetInstance()->ReleaseSpanToPageCache(span);
            PageCache::GetInstance()->_pageMtx.unlock();
        }
        else
        {
            assert(pTLSThreadCache);
            pTLSThreadCache->Deallocate(ptr, size);
        }
    }
}
