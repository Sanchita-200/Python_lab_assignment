"""
Consider the following linear equations and solve using sci-py.
2x + 3y =8 & 4x+5y =14
Consider a scenario where 2 cars (A,B) are moving, A from point P, B from point Q in the same direction and meet each other after 11 hours. 
If they move in the opposite direction, they will meet after 1 hour. Find out the velocity of both cars.
"""
import numpy as np
import scipy.linalg as la

#1: Linear Equations:
coeffs = np.array([[2, 3], 
                   [4, 5]])
constants = np.array([8, 14])

solution_xy = la.solve(coeffs, constants)
print(f"Solution to equations: x = {solution_xy[0]}, y = {solution_xy[1]}")

#2: Car Scenario (Assuming distance d = 110 km):
# 11*v_A - 11*v_B = 110
# 1*v_A  + 1*v_B  = 110
car_coeffs = np.array([[11, -11], 
                       [1, 1]])
distance = np.array([110, 110])

velocities = la.solve(car_coeffs, distance)
print(f"Velocity of Car A: {velocities[0]} km/h")
print(f"Velocity of Car B: {velocities[1]} km/h")
