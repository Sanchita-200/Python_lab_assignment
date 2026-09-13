"""
Create a matrix of 4x4 order and find out the transpose of the matrix and the rank of the matrix using sci-py.
CS4- Create a sqaure matrix of 4x4 order. 
Find out the eigen value and eigen vector of this matrix.
Find out Permutation Matrix (P),Lower Triangular Matrix (L) and Upper Triangular Matrix (U) of the matrix.
"""
import numpy as np
import scipy.linalg as la

M4 = np.array([[4, 1, 1, 2], , 
, 
              [2, 1, 1, 5]])

eigenvalues, eigenvectors = la.eig(M4)
P, L, U = la.lu(M4)

print("Eigenvalues:\n", eigenvalues)
print("\nEigenvectors:\n", eigenvectors)
print("\nPermutation Matrix (P):\n", P)
print("\nLower Triangular Matrix (L):\n", L)
print("\nUpper Triangular Matrix (U):\n", U)
