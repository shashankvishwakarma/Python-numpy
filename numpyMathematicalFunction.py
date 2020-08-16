import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])
print(a.min())
print(a.max())
print(a.sum())

# axis 0 will be columns and axis 1 will be rows
print(a.sum(axis=0))
print(a.sum(axis=1))

print(np.sqrt(a))
print(np.square(a))
print(np.std(a))

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print("addition operation: ", a + b)
print("multiplication operation: ", a * b)
print("division operation: ", a / b)

print("multiplication of matrix: ", a.dot(b))
