//#define _CRT_SECURE_NO_WARNINGS
//// test_alloc.cpp
//#include <iostream>
//#include <chrono>
//#include <vector>
//#include <cstdlib>
//#include "ConcurrentAlloc.h"
//
//void test_system_malloc(size_t n) {
//    std::vector<void*> ptrs(n);
//
//    auto start = std::chrono::high_resolution_clock::now();
//    for (size_t i = 0; i < n; ++i) {
//        ptrs[i] = malloc(128); // 分配128字节
//    }
//    auto end = std::chrono::high_resolution_clock::now();
//    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
//    std::cout << "System malloc time: " << duration.count() << "ms\n";
//
//    start = std::chrono::high_resolution_clock::now();
//    for (size_t i = 0; i < n; ++i) {
//        free(ptrs[i]);
//    }
//    end = std::chrono::high_resolution_clock::now();
//    duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
//    std::cout << "System free time: " << duration.count() << "ms\n";
//}
//
//void test_custom_alloc(size_t n) {
//    std::vector<void*> ptrs(n);
//
//    auto start = std::chrono::high_resolution_clock::now();
//    for (size_t i = 0; i < n; ++i) {
//        ptrs[i] = ConcurrentAlloc(128); // 分配128字节
//    }
//    auto end = std::chrono::high_resolution_clock::now();
//    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
//    std::cout << "Custom alloc time: " << duration.count() << "ms\n";
//
//    start = std::chrono::high_resolution_clock::now();
//    for (size_t i = 0; i < n; ++i) {
//        ConcurrentFree(ptrs[i]);
//    }
//    end = std::chrono::high_resolution_clock::now();
//    duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start);
//    std::cout << "Custom free time: " << duration.count() << "ms\n";
//}
//
//int main() {
//    size_t n = 100000; // 分配和释放的次数
//    std::cout << "Testing system malloc/free...\n";
//    test_system_malloc(n);
//
//    std::cout << "Testing custom allocator...\n";
//    test_custom_alloc(n);
//
//    return 0;
//}
