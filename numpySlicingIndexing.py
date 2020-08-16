import numpy as np

n = np.array([6, 7, 8])
print("slicing: ", n[0:2])
print("last element: ", n[-1])

a = np.array([[6, 7, 8], [1, 2, 3], [9, 3, 2]])
print("indexing: ", a[1, 2])
print(a[0:2, 2])  # slicing and indexing 2nd element
print(a[-1, 0:2])  # last row print 0-2

# iteration
a = np.array([[6, 7, 8], [1, 2, 3], [9, 3, 2]])
'''
for row in a:
    print(row)

for cell in a.flat:
    print(cell)
'''
for cell in a.flatten():
    print(cell)

for cell in np.nditer(a, order="C"):  # print column wise - "C Order"
    print(cell)

for cell in np.nditer(a, order="F"):  # print row wise - "Fortran Order"
    print(cell)

a = np.arange(6).reshape(3, 2)
b = np.arange(6, 12).reshape(3, 2)
print("vertical stacking: ", np.vstack((a, b)))
print("horizontal stacking: ", np.hstack((a, b)))

# split
a = np.arange(30).reshape(2, 15)
result = np.hsplit(a, 3)
print(result[0])
print(result[1])
print(result[2])

result = np.vsplit(a, 2)
print(result[0])
print(result[1])

a = np.arange(12).reshape(3, 4)
b = a > 4
print(b)
print(a[b])  # it will return where it is true
