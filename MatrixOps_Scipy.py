"""
Create a matrix of 4x4 order and find out the transpose of the matrix and the rank of the matrix using sci-py.
"""
import numpy as np

M3 = np.array([[1, 2, 3, 4], , 
, 
              [13, 14, 15, 16]])

M3_transpose = M3.T
matrix_rank = np.linalg.matrix_rank(M3)

print("Transpose Matrix:\n", M3_transpose)
print(f"\nRank of the Matrix: {matrix_rank}")
