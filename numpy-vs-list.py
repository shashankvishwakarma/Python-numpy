import numpy as np
import sys
import time

# showing np array uses less memory
list = range(1000)
print(sys.getsizeof(1) * len(list))

array = np.arange(1000)
print(array.size * array.itemsize)

# showing np array is faster and convenient when compared to list
SIZE = 1000000
list1 = range(SIZE)
list2 = range(SIZE)

array1 = np.arange(SIZE)
array2 = np.arange(SIZE)

# Python list
start = time.time()
result = [(x + y) for x, y in zip(list1, list2)]
print("python list took: ", (time.time() - start) * 1000)

# Python numpy array
start = time.time()
result = array1 + array2
print("python numpy took: ", (time.time() - start) * 1000)
