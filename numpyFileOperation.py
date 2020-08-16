import numpy as np
import csv

# np.set_printoptions(threshold=6)
# np.set_printoptions(threshold=np.nan)

# Turn off scientific notation
# np.set_printoptions(suppress=True)

with open('datasets\winequality-red.csv', 'r') as f:
    wines = list(csv.reader(f, delimiter=';'))
# print(wines[:3])
wines = np.array(wines[1:], dtype=np.float)

# print(wines)
print('wines shape', wines.shape)
print('wines ndim', wines.ndim)

wines = np.genfromtxt("datasets\\winequality-red.csv", delimiter=";", skip_header=1)
# print('wines using numpy \n',wines)

print('================== Slicing NumPy Arrays... ============================')
# Slicing NumPy Arrays...
print('2nd row 3rd column', wines[2, 3])
print(wines[0:3, 3])

print('================== Assigning Values To NumPy Arrays... ============================')
# Assigning Values To NumPy Arrays...
print(wines[1, 5])
wines[1, 5] = 10
print(wines[1, 5])

print('================== Converting Data Types... ============================')
# Converting Data Types
int_wines = wines.astype(int)
# print('Converting Data Types to int \n',int_wines)

data = np.genfromtxt('datasets\\auto.csv', delimiter=',', skip_header=1, filling_values=-999, dtype='float')
print(data[:3])  # see first 3 rows

# Save the array as a csv file
np.savetxt("datasets\out.csv", data, delimiter=",")
