# # model.py
# import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense
# import numpy as np

# print("Starting model script...")

# # 创建一个简单的模型
# model = Sequential([
#     Dense(4, activation='relu', input_shape=(4,)),
#     Dense(4, activation='relu'),
#     Dense(1, activation='linear')
# ])

# print("Model script loaded successfully.")

# def predict(input_data):
#     input_data = np.array(input_data).reshape(-1, 4)
#     prediction = model.predict(input_data)
#     return prediction.flatten().tolist()


# import tensorflow as tf
# import numpy as np
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense

# # 创建一个简单的模型
# def create_model():
#     model = Sequential([
#         Dense(10, activation='relu', input_shape=(4,)),
#         Dense(1, activation='sigmoid')
#     ])
#     model.compile(optimizer='adam', loss='mse')
#     return model

# # 模拟训练一个简单的模型（这里用随机数据）
# def train_model(model):
#     x_train = np.random.random((100, 4))
#     y_train = np.random.random((100, 1))
#     model.fit(x_train, y_train, epochs=5)

# # 进行预测
# def predict(input_data):
#     model = create_model()
#     train_model(model)
#     result = model.predict(np.array([input_data]))
#     return result[0][0]

# if __name__ == "__main__":
#     print("Starting Python...")
#     input_data = [1.0, 2.0, 3.0, 4.0]  # 示例输入数据
#     result = predict(input_data)
#     print(f"Prediction result: {result}")








# import tensorflow as tf
# import numpy as np
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense
# import ctypes

# # 加载C++库
# lib = ctypes.CDLL('D:/cs/C++/CPP/GBF/Project1/Project1/build/Debug/my_custom_allocator.dll')

# # 定义C++函数的接口
# lib.ConcurrentAlloc.restype = ctypes.c_void_p
# lib.ConcurrentAlloc.argtypes = [ctypes.c_size_t]

# lib.ConcurrentFree.restype = None
# lib.ConcurrentFree.argtypes = [ctypes.c_void_p]

# # 创建一个简单的模型
# def create_model():
#     model = Sequential([
#         Dense(10, activation='relu', input_shape=(4,)),
#         Dense(1, activation='sigmoid')
#     ])
#     model.compile(optimizer='adam', loss='mse')
#     return model

# # 模拟训练一个简单的模型（这里用随机数据）
# def train_model(model):
#     x_train = np.random.random((100, 4)).astype(np.float32)
#     y_train = np.random.random((100, 1)).astype(np.float32)

#     # 使用C++内存分配器分配内存
#     x_train_ptr = lib.ConcurrentAlloc(x_train.nbytes)
#     y_train_ptr = lib.ConcurrentAlloc(y_train.nbytes)

#     # 将numpy数组数据复制到C++分配的内存中
#     ctypes.memmove(x_train_ptr, x_train.ctypes.data, x_train.nbytes)
#     ctypes.memmove(y_train_ptr, y_train.ctypes.data, y_train.nbytes)

#     # 从C++内存指针创建TensorFlow张量
#     x_train_tf = tf.constant(np.frombuffer(ctypes.string_at(x_train_ptr, x_train.nbytes), dtype=np.float32).reshape((100, 4)))
#     y_train_tf = tf.constant(np.frombuffer(ctypes.string_at(y_train_ptr, y_train.nbytes), dtype=np.float32).reshape((100, 1)))

#     model.fit(x_train_tf, y_train_tf, epochs=5)

#     # 释放C++内存
#     lib.ConcurrentFree(x_train_ptr)
#     lib.ConcurrentFree(y_train_ptr)

# # 进行预测
# def predict(input_data):
#     model = create_model()
#     train_model(model)
#     result = model.predict(np.array([input_data]))
#     return result[0][0]

# if __name__ == "__main__":
#     print("Starting Python...")
#     input_data = [1.0, 2.0, 3.0, 4.0]  # 示例输入数据
#     result = predict(input_data)
#     print(f"Prediction result: {result}")

# 上面这个是可以跑起来的
# import tensorflow as tf
# import numpy as np
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense
# import ctypes
# import time

# # 加载C++库
# lib = ctypes.CDLL('D:/cs/C++/CPP/GBF/Project1/Project1/build/Debug/my_custom_allocator.dll')

# # 定义C++函数的接口
# lib.ConcurrentAlloc.restype = ctypes.c_void_p
# lib.ConcurrentAlloc.argtypes = [ctypes.c_size_t]

# lib.ConcurrentFree.restype = None
# lib.ConcurrentFree.argtypes = [ctypes.c_void_p]

# # 创建一个简单的模型
# def create_model():
#     model = Sequential([
#         Dense(10, activation='relu', input_shape=(4,)),
#         Dense(1, activation='sigmoid')
#     ])
#     model.compile(optimizer='adam', loss='mse')
#     return model

# # 模拟训练一个简单的模型（这里用随机数据）
# def train_model(model):
#     x_train = np.random.random((100, 4)).astype(np.float32)
#     y_train = np.random.random((100, 1)).astype(np.float32)

#     # 使用C++内存分配器分配内存
#     x_train_ptr = lib.ConcurrentAlloc(x_train.nbytes)
#     y_train_ptr = lib.ConcurrentAlloc(y_train.nbytes)

#     # 将numpy数组数据复制到C++分配的内存中
#     ctypes.memmove(x_train_ptr, x_train.ctypes.data, x_train.nbytes)
#     ctypes.memmove(y_train_ptr, y_train.ctypes.data, y_train.nbytes)

#     # 从C++内存指针创建TensorFlow张量
#     x_train_tf = tf.constant(np.frombuffer(ctypes.string_at(x_train_ptr, x_train.nbytes), dtype=np.float32).reshape((100, 4)))
#     y_train_tf = tf.constant(np.frombuffer(ctypes.string_at(y_train_ptr, y_train.nbytes), dtype=np.float32).reshape((100, 1)))

#     model.fit(x_train_tf, y_train_tf, epochs=5)

#     # 释放C++内存
#     lib.ConcurrentFree(x_train_ptr)
#     lib.ConcurrentFree(y_train_ptr)

# # 进行预测
# def predict(input_data):
#     model = create_model()
#     train_model(model)
#     result = model.predict(np.array([input_data]))
#     return result[0][0]

# if __name__ == "__main__":
#     print("Starting Python with C++ custom allocator version...")
#     start_time = time.time()
#     input_data = [1.0, 2.0, 3.0, 4.0]  # 示例输入数据
#     result = predict(input_data)
#     end_time = time.time()
#     print(f"Prediction result: {result}")
#     print(f"Training and prediction time: {end_time - start_time} seconds")



import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import ctypes
import time

# 加载C++库
try:
    lib = ctypes.CDLL('D:/cs/C++/CPP/GBF/Project1/Project1/build/Debug/my_custom_allocator.dll')
    print("C++ library loaded successfully.")
except Exception as e:
    print(f"Failed to load C++ library: {e}")

# 定义C++函数的接口
try:
    lib.ConcurrentAlloc.restype = ctypes.c_void_p
    lib.ConcurrentAlloc.argtypes = [ctypes.c_size_t]
    
    lib.ConcurrentFree.restype = None
    lib.ConcurrentFree.argtypes = [ctypes.c_void_p]
    print("C++ functions defined successfully.")
except Exception as e:
    print(f"Failed to define C++ functions: {e}")

# 创建一个简单的模型
def create_model():
    try:
        model = Sequential([
            Dense(10, activation='relu', input_shape=(4,)),
            Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam', loss='mse')
        print("Model created successfully.")
        return model
    except Exception as e:
        print(f"Model creation failed: {e}")
        return None

# 模拟训练一个简单的模型（这里用随机数据）
def train_model(model):
    try:
        x_train = np.random.random((100000, 4)).astype(np.float32)
        y_train = np.random.random((100000, 1)).astype(np.float32)

        # 使用C++内存分配器分配内存
        try:
            x_train_ptr = lib.ConcurrentAlloc(x_train.nbytes)
            y_train_ptr = lib.ConcurrentAlloc(y_train.nbytes)
            print("Memory allocated using C++ allocator.")
        except Exception as e:
            print(f"Memory allocation failed: {e}")
            return False  # 退出函数，防止后续出错

        # 将numpy数组数据复制到C++分配的内存中
        try:
            ctypes.memmove(x_train_ptr, x_train.ctypes.data, x_train.nbytes)
            ctypes.memmove(y_train_ptr, y_train.ctypes.data, y_train.nbytes)
            print("Memory copied to C++ allocated memory.")
        except Exception as e:
            print(f"Memory copy failed: {e}")
            return False  # 退出函数，防止后续出错

        # 从C++内存指针创建TensorFlow张量
        try:
            x_train_tf = tf.constant(np.frombuffer(ctypes.string_at(x_train_ptr, x_train.nbytes), dtype=np.float32).reshape((100000, 4)))
            y_train_tf = tf.constant(np.frombuffer(ctypes.string_at(y_train_ptr, y_train.nbytes), dtype=np.float32).reshape((100000, 1)))
            print("TensorFlow tensors created from C++ allocated memory.")
        except Exception as e:
            print(f"Tensor creation failed: {e}")
            return False  # 退出函数，防止后续出错

        try:
            model.fit(x_train_tf, y_train_tf, epochs=5)
            print("Model training completed.")
        except Exception as e:
            print(f"Model training failed: {e}")
            return False  # 退出函数，防止后续出错

        # 释放C++内存
        try:
            lib.ConcurrentFree(x_train_ptr)
            lib.ConcurrentFree(y_train_ptr)
            print("Memory freed using C++ allocator.")
        except Exception as e:
            print(f"Memory free failed: {e}")

        return True
    except Exception as e:
        print(f"Unexpected error during training: {e}")
        return False

# 进行预测
def predict(input_data):
    model = create_model()
    if model is None:
        print("Model creation failed in predict function.")
        return None
    if not train_model(model):
        print("Model training failed in predict function.")
        return None
    try:
        result = model.predict(np.array([input_data]))
        print("Model prediction completed.")
        return result[0][0]
    except Exception as e:
        print(f"Prediction failed: {e}")
        return None

if __name__ == "__main__":
    print("Starting Python with C++ custom allocator version...")
    try:
        start_time = time.time()
        input_data = [1.0, 2.0, 3.0, 4.0]  # 示例输入数据
        result = predict(input_data)
        end_time = time.time()
        if result is not None:
            print(f"Prediction result: {result}")
        else:
            print("Prediction failed.")
        print(f"Training and prediction time: {end_time - start_time} seconds")
    except Exception as e:
        print(f"Error during prediction: {e}")





