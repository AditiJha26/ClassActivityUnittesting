# Aditi Jha
# CS 230
# Week 2 Lab 01

import math
import unittest
from main import Rectangle, Circle

class TestRectangleMethods(unittest.TestCase):

    def setUp(self):
        # Setting up a Rectangle for testing
        self.rectangle = Rectangle(name="MyRectangle", width=3, height=4)

    def test_area(self):
        # Testing if the area method returns the correct value
        result = self.rectangle.area()
        self.assertEqual(result, 12)  # 3 * 4 = 12

    def test_area_zero(self):
        # Testing if the area method handles zero values correctly
        rectangle_with_zero = Rectangle(name="ZeroRectangle", width=0, height=5)
        result = rectangle_with_zero.area()
        self.assertEqual(result, 0)  # 0 * 5 = 0

class TestCircleMethods(unittest.TestCase):

    def setUp(self):
        # Setting up a Circle for testing
        self.circle = Circle(name="MyCircle", radius=5)

    def test_area(self):
        # Testing if the area method returns the correct value
        result = self.circle.area()
        expected_area = math.pi * (5 ** 2)  # π * 5^2
        self.assertAlmostEqual(result, expected_area, places=5)

    def test_area_zero(self):
        # Testing if the area method handles zero radius correctly
        circle_with_zero_radius = Circle(name="ZeroCircle", radius=0)
        result = circle_with_zero_radius.area()
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()
