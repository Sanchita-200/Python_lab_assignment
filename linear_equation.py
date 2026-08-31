'''
Consider two equations:
1. 3x = 5y + 10
2. 4x - 2y = 7
find the value od x and y using numpy package.
'''

import numpy as np

A = np.array([
    [3, -5],
    [4, -2]
])

B = np.array([10, 7])

x, y = np.linalg.solve(A, B)

print("x =", x)
print("y =", y)