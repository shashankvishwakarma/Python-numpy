import numpy as np

# Create an array
arr_rand = np.array([8, 8, 3, 7, 7, 0, 4, 2, 5, 2])
print("Array: ", arr_rand)

# Positions where value > 5
index_gt5 = np.where(arr_rand > 5)
print("Index where value > 5: ", index_gt5)

# Take items at given index
print('Take items at given index',arr_rand.take(index_gt5))

# Location of the max
print('Position of max value: ', np.argmax(arr_rand))

# Location of the min
print('Position of min value: ', np.argmin(arr_rand))

dt = np.dtype([('age',np.int8)])
a = np.array([(10,),(20,),(30,)], dtype = dt)
print("Age: ", a['age'])

empty_array = np.empty([3,2], dtype = int)
print("Empty Array: \n", empty_array)

a = np.zeros([4, 4])
b = np.ones([4, 4])
#print(a)
#print(b)

# Vertical Stack Equivalents (Row wise)
print('Vertical Stack Equivalents (Row wise) concatenate \n',np.concatenate([a, b], axis=0))
print('Vertical Stack Equivalents (Row wise) vstack \n',np.vstack([a,b]))
print('Vertical Stack Equivalents (Row wise) r_ \n',np.r_[a,b])

# Horizontal Stack Equivalents (column wise)
print('Horizontal Stack Equivalents (Coliumn wise) concatenate \n ',np.concatenate([a, b], axis=1))
print('Horizontal Stack Equivalents (Coliumn wise) hstack \n ',np.hstack([a,b]))
print('Horizontal Stack Equivalents (Coliumn wise) c_ \n ',np.c_[a,b])
