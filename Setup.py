import torch
import torch.nn as nn
import torch.optim as optim
import time
from memory_profiler import memory_usage
import ctypes

# 导入自定义内存分配器模块
memory_allocator = ctypes.CDLL('./memory_allocator.dll')

# 定义自定义内存分配器的分配和释放函数
allocate_memory = memory_allocator.allocate_memory
allocate_memory.restype = ctypes.c_void_p
allocate_memory.argtypes = [ctypes.c_size_t]

deallocate_memory = memory_allocator.deallocate_memory
deallocate_memory.restype = None
deallocate_memory.argtypes = [ctypes.c_void_p]

# 定义简单的神经网络
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(784, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)

    def forward(self, x):
        x = torch.flatten(x, 1)
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# 初始化网络、损失函数和优化器
model = SimpleNet()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

# 模拟训练数据
data = torch.randn(64, 1, 28, 28)
target = torch.randint(0, 10, (64,))

# 测试内存使用和时间
def train(use_custom_allocator=False):
    if use_custom_allocator:
        ptr = allocate_memory(1024 * 1024 * 10)  # 分配10MB内存
    optimizer.zero_grad()
    output = model(data)
    loss = criterion(output, target)
    loss.backward()
    optimizer.step()
    if use_custom_allocator:
        deallocate_memory(ptr)  # 释放内存

# 包装函数以适应 memory_usage 调用
def train_with_standard_allocator():
    train(use_custom_allocator=False)

def train_with_custom_allocator():
    train(use_custom_allocator=True)

# if __name__ == "__main__":
#     mem_usage_standard = memory_usage(train_with_standard_allocator)
#     start_time_standard = time.time()
#     for epoch in range(10):
#         train_with_standard_allocator()
#     end_time_standard = time.time()

    # print(f'Standard Allocator - Memory usage: {max(mem_usage_standard)} MB')
    # print(f'Standard Allocator - Time taken: {end_time_standard - start_time_standard} seconds')
if __name__ == "__main__":
    mem_usage_custom = memory_usage(train_with_custom_allocator)
    start_time_custom = time.time()
    for epoch in range(10):
        train_with_custom_allocator()
    end_time_custom = time.time()

    print(f'Custom Allocator - Memory usage: {max(mem_usage_custom)} MB')
    print(f'Custom Allocator - Time taken: {end_time_custom - start_time_custom} seconds')
