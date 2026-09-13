"""
Create a class triangle with 3 variables side1, side2, side3.
Initialize the variables with constructor.
It also has the variables angle1, angle2, angle3.
Create a class equilateral triangle and find the area of the triangle using calArea() function.
Find the tangent of all angles using find angles method.
Create a class scalene which is a child of triangle class.
Find out the perimeter of the triangle using calPerimeter() function.
Find out the area of the triangle using calArea() function.
Use the math package for the computation.
Print the area as a whole number.
"""

import math as m

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.angle1 = None
        self.angle2 = None
        self.angle3 = None

class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)
        # All angles in an equilateral triangle are 60 degrees (converted to radians)
        self.angle1 = m.radians(60)
        self.angle2 = m.radians(60)
        self.angle3 = m.radians(60)

    def calArea(self):
        # Area formula for equilateral triangle: (sqrt(3)/4) * side^2
        area = (m.sqrt(3) / 4) * (self.side1 ** 2)
        return round(area)

    def find_angles(self):
        # Calculates and displays the tangent of all angles
        tan1 = m.tan(self.angle1)
        tan2 = m.tan(self.angle2)
        tan3 = m.tan(self.angle3)
        print(f"Tangent of Angle 1: {tan1:.4f}")
        print(f"Tangent of Angle 2: {tan2:.4f}")
        print(f"Tangent of Angle 3: {tan3:.4f}")

class Scalene(Triangle):
    def __init__(self, side1, side2, side3):
        super().__init__(side1, side2, side3)

    def calPerimeter(self):
        return self.side1 + self.side2 + self.side3

    def calArea(self):
        # Area using Heron's Formula
        s = self.calPerimeter() / 2  # Semi-perimeter
        area = m.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return round(area)  


print("--- Equilateral Triangle Details ---")
eq_tri = EquilateralTriangle(6)
print(f"Area: {eq_tri.calArea()}")
eq_tri.find_angles()

print("\n--- Scalene Triangle Details ---")
scal_tri = Scalene(3, 4, 5)
print(f"Perimeter: {scal_tri.calPerimeter()}")
print(f"Area: {scal_tri.calArea()}")
