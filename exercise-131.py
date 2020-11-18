import numpy as np


np.random.seed(seed=60)
random_square = np.random.rand(5, 5)
# full matrix
print(random_square)
# first row
print(random_square[0])
print(random_square[0, :])
# first column
print(random_square[:, 0])
# first entry
print(random_square[0, 0])
print(random_square[0][0])
# third entry, fourth column
print(random_square[2, 3])

# mean of entire matrix
print(random_square.mean())
# mean of first row
print(random_square[0].mean())
# mean of last column
print(random_square[:, -1].mean())
