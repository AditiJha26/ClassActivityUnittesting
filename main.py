# Aditi Jha
# CS 230
# Week 2 Lab 01

import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

