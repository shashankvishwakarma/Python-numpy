import numpy as np

a = np.array([1, 2, 3])
print(a[1])

# 2D array
a = np.array([[1, 2, 3], [4, 5, 6]])
print("dimension: ", a.ndim)
print("item size: ", a.itemsize)
print("data type: ", a.dtype)

# changing datatype to float
a = np.array([[1, 2], [3, 4], [5, 6]], dtype=np.float64)
print("data type: ", a.dtype)
print("size: ", a.size)
print("shape: ", a.shape)

a = a.reshape(2, 3)
print("after reshape: ", a)
print("shape: ", a.shape)

a = a.ravel()
print("after ravel: ", a)

array = np.arange(1, 5)
print("array using arange: ", array)
array = np.arange(1, 15, 2)
print("array using arange with step increment 2: ", array)

array = np.linspace(1, 5, 10)

# changing datatype to complex
a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.complex)
print(a)

# Create an array
arr_rand = np.array([8, 8, 3, 7, 7, 0, 4, 2, 5, 2])
print("Array: ", arr_rand)

# Positions where value > 5
index_gt5 = np.where(arr_rand > 5)
print("Index where value > 5: ", index_gt5)

# Take items at given index
print('Take items at given index', arr_rand.take(index_gt5))

# Location of the max
print('Position of max value: ', np.argmax(arr_rand))

# Location of the min
print('Position of min value: ', np.argmin(arr_rand))

dt = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype=dt)
print("Age: ", a['age'])

empty_array = np.empty([3, 2], dtype=int)
print("Empty Array: \n", empty_array)

a = np.zeros((4, 4))
b = np.ones((4, 4))
print(a)
print(b)
