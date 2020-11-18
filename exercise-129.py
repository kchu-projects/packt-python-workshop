import numpy as np


income = np.array([75000, 55000, 88000, 125000, 64000, 97000])
print(income.mean())

income = np.append(income, 12000000)
print(income.mean())

print(np.median(income))
