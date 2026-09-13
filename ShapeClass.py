"""
Create a class Shape with variable 'radius'.
Initialize the variable with constructor.
Define a method calArea() to calculate the arae of the circle using math package.
Create a class Sphere which is a child of shape class.
Define calVolume() to calculate the volume of the sphere.
"""

import math as m

class Shape:
    def __init__(self, r):
        self.radius = r 
        
    def calArea(self):
        return m.pi * (self.radius ** 2)

class Sphere(Shape):
    def __init__(self, r):
        super().__init__(r) 
        
    def calVolume(self):
        return (4/3) * m.pi * (self.radius ** 3)


my_sphere = Sphere(5)

print(f"Radius: {my_sphere.radius}")
print(f"Circle Area: {my_sphere.calArea():.2f}")
print(f"Sphere Volume: {my_sphere.calVolume():.2f}")
