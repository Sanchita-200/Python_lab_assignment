import numpy as np

A = np.array([[1, 2, 3], , 
              [5, 6, 0]])

B = np.array([[2, 0, 1], , 
              [1, 2, 4]])

A_inv = np.linalg.inv(A)
det_B = np.linalg.det(B)
A_dot_A_inv = np.dot(A, A_inv)

print("Inverse of A:\n", A_inv)
print("\nDeterminant of B:", det_B)
print("\nResult of A . A_inv:\n", np.round(A_dot_A_inv))
