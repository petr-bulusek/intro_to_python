# -*- coding: utf-8 -*-
"""
@author: petr bulusek
"""

# this is often used in import
import numpy as np

a = np.array([1, 2, 3])

# numpy array has some type
a.dtype
# and shape
a.shape

# you can specify type by creating
a = np.array([1, 2, 3], dtype=float)

# most generall type is 'object'

# types are related to C implementation under the hood
# numpy can do vectorization on operations


# we can create numpy matrix from list of lists

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a.shape

# numpy has functions for creating special matrices
a = np.zeros((2,3))  # with zeros
e = np.eye(3)  # unit matrix, unit matrix can be only nxn, so we specify only one dimension
d = np.diag([1, 2, 3, 4])
f = np.full((4, 4), 2.0)

# for integer values np.arange, similar to normal python range function
np.arange

# for floats it is better to use linspace
start = 0
stop = 10
numpoints = 1000
x = np.linspace(start, stop, numpoints)


# indexing
a[0]
a[0][0]
a[0, 0]

a[:, 1]  # second column

# reshape
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
reshaped = a.reshape((2, 6))

# be carefull when reference or view is created
# some functions take inplace argument
# if you need copy, use .copy()
reshaped = a.reshape((2, 6)).copy()

# logical indexing
a > 5
a[a > 5]

# operations are elementwise
a + 1
a * 2

# even multiplication
# if you need matrix multiplication, use @ operator
a @ a
a @ a.T


# functions work vectorwise
start = 0
stop = 10
numpoints = 1000
x = np.linspace(start, stop, numpoints)
y = np.sin(x)

# linear algebra
np.linalg

# random module
np.random

# broadcasting
# cannot do with  math.sin

import matplotlib.pyplot as plt
# use in console %matplotlib qt5
x = np.linspace(0, 10, 1000)
y = np.sin(x)

plt.xlabel('x')
plt.ylabel('sin(x)')
plt.plot(x, y)
