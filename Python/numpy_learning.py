# Why is NumPy used?
# -> It supports much faster operations with vectors / matrices etc compared to Python data structures
# -> Supports multidimensional arrays: 1D, 2D, etc
# -> Contains huge functionality for Linear Algebra, Statistics, Vectors, etc
# -> Integrates well with the Pandas, Scikit-Learn and Scientific Python ecosystem



import numpy as np


array = np.array([1, 2, 3, 4])
print(type(array))              # Prints <class 'numpy.ndarray'>


# Python List vs Numpy Array:

a = [1, 2, 3]                   # Inconvenient for Scalar Multiplication
print(a * 2)                    # Gives [1, 2, 3, 1, 2, 3]                    

a = np.array([1, 2, 3])
print(a * 2)                    # Gives [2, 4, 6], an gives it FAST

# Multi-dimensional Arrays

a = np.array(0)
print(a.ndim)                   # 0 Dimension: Meaning a point

a = np.array([1, 2, 3]) 
print(a.ndim)                   # 1: Meaning a line

a = np.array([[1, 2, 3], 
              [4, 5, 6]]) 
print(a.ndim)                   # 2: Meaning a 2D Plane

a = np.array([[[1, 2, 3], [4, 5, 6]],
              [[7, 8, 9], [10, 11, 12]],
              [[13, 14, 15], [16, 17, 18]]])

print(a.ndim)                   # 3: Meaning a 3D Space

# Remember that the consequent 2D Layers must be consistent, otherwise there will be an error

print(a.shape)

# Prints (3, 2, 3) -> Meaning 3 Layers, 2 Rows, 3 Columns

# Multi-dimensional Indexing instead of chain indexing is used, i.e a[0][1][2] = a[0, 1, 2]
# Much faster than chain indexing


# SLICING: Select anything in a numpy array, rows, columns, quadrants, etc

# format: array[rowstart:rowend + 1:step, colstart:colend + 1:step]

a = np.array([['A', 'B', 'C'],
             ['D', 'E', 'F'],
             ['G', 'H', 'I']])

print(a[0, :])             # Select 0th row
print(a[:, 0])             # Select 0th column

print(a[0:2, 0:2])         # Took a sub-matrix out

print(a[::-1, ::-1])       # Rotated along a corner

print(a[::-1, :])          # Reverse Rows


# Scalar Arithmetic

a = np.array([1, 2, 3])
print(a * 2)
print(a + 1)
print(a ** 4)
print(a // 2)
print(a / 2)

# Vectorized Math Functions

a = np.array([1, 2, 3, 4])
print(np.sqrt(a))
print(np.round(a / 2))

# Example: Calculate Area for a circle, from given set of radii

radii = np.array([0.5, 1, 2])
print(np.pi * radii ** 2)

# Vector Arithmetic

a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])

print(a1 + a2)
print(a1 * a2)

# Comparison Operator

scores = np.array([100, 90, 84, 98, 23, 56, 12, 78])

scores[scores < 30] = 0
print(scores)
cgpa = scores / 10
print(cgpa)

# Broadcasting in NumPy:

array1 = np.array([1, 2, 3])         # Shape: (3, )

array2 = np.array([[1], [2], [3]])   # Shape: (3, 1)

# Broadcasting Rules:
# For every dimension (taken from right to left, if less dimensions and 1 assigned to missing dims)
# Either in both arrays it should be same or any one of them is 1

# In the above example,
# the comparison is as follows:
# (3, ) -> right -> (, 3) -> (1, 3)
# (3, 1)                  -> (3, 1) -> Both are broadcastable

# Thus, NumPy virtually extends the dimensions of the smaller array to fit the operation

print(array1 + array2)

# Result: [[2 3 4]
#          [3 4 5]
#          [4 5 6]]

# Scaler arithmetic is an example of Broadcasting Too

# Aggregate Functions: Return one value from an array

a = np.array([[1, 2, 3, 4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15, 16]])
print(np.min(a))            # Min value: 1
print(np.argmax(a))         # Flattens the array: Returns 15

print(np.mean(array))
print(np.var(array))
print(np.std(array))

print(np.mean(a[:, 0]))     # Mean of 1st column: 1 + 9 / 2 = 5.0
# Above example uses chain indexing + slicing + aggregate function

# Filtering

ages = np.array([[18, 19, 20, 17],
                 [16, 18, 21, 23]])

newages = ages[(ages >= 18) & (ages < 21)]
print(newages)              # Flattens the array


# Also NumPy has a lot of random number generation / manipulation functionalities
# using np.random, can visit the official documentation for further information

