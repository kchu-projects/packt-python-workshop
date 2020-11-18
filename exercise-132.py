import numpy as np


print(np.arange(1, 101))
print(np.arange(1, 101).reshape(20, 5))

mat1 = np.arange(1, 101).reshape(20, 5)
# subtract 50 from each element
print(mat1 - 50)
# multiply 10 to each element
print(mat1 * 10)
# add each element to itself
print(mat1 + mat1)
# multiply each element to itself
print(mat1 * mat1)
# get dot product of matrix with its transpose
print(np.dot(mat1, mat1.T))
