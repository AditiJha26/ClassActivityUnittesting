# Aditi Jha
# CS 230
# Week 2 Lab 01

import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass
    def perimeter(self):
        pass
    def compare_area(self, other_shape):
        if self.area() > other_shape.area():
            return f"{self.name} has a larger area than {other_shape.name}."
        elif self.area() < other_shape.area():
            return f"{other_shape.name} has a larger area than {self.name}."
        else:
            return f"{self.name} and {other_shape.name} have the same area."


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (2 * self.width) + (2 * self.height)

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        return (2 * math.pi * self.radius)

