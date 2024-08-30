# Aditi Jha
# CS 230
# Week 2 Lab 01

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
