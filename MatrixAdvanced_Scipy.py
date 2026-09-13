"""
Consider a square matrix and use the following methods, print the results and give explanation.
qr()
svd()
lstsq()
"""
import numpy as np
import scipy.linalg as la

M5 = np.array([[2, -1, 0], 
              [1, 2, -3], 
              [0, 1, 2]])
b = np.array([1, 2, 3])

Q, R = la.qr(M5)
U, S, Vt = la.svd(M5)
x_lstsq, residuals, rank, s_vals = la.lstsq(M5, b)

print("QR Decomposition - Q:\n", Q, "\nR:\n", R)
print("\nSVD - U:\n", U, "\nS:\n", S, "\nVt:\n", Vt)
print("\nLeast-Squares Solution:\n", x_lstsq)

"""
Method Description:
qr() -> QR Decomposition factorises a matrix into an orthogonal matrix (Q) and an upper triangular matrix (R). It is used for linear system solving and numerical stability.

svd() -> Singular Value Decomposition factors a matrix into components reflecting rotation (U), scaling (Σ), and rotation (V**T). It assists with dimensionality reduction and data noise filtering.

lstsq() -> Least-Squares Solver computes the closest logical approximation for overdetermined systems (Ax = b) by minimising residual error geometric distance.
"""
