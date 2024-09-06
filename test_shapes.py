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
        
    def test_perimeter(self):
        result = self.rectangle.perimeter()
        self.assertEqual(result,14)

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
        
    def test_perimeter(self):
        result = self.circle.perimeter()
        expected_area = math.pi * 5 * 2
        self.assertEqual(result, expected_area)

class TestCompareArea(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle(name="Rectangle", width=3, height=4)  # Area = 12
        self.circle = Circle(name="Circle", radius=5)  # Area ≈ 78.54

    def test_compare_area_circle_larger(self):
        # Circle area (π*5^2 ≈ 78.54) is larger than the rectangle area (12)
        result = self.circle.compare_area(self.rectangle)
        self.assertEqual(result, "Circle has a larger area than Rectangle.")

    def test_compare_area_rectangle_smaller(self):
        # Rectangle area is 12, Circle area is larger than that
        result = self.rectangle.compare_area(self.circle)
        self.assertEqual(result, "Circle has a larger area than Rectangle.")

    def test_compare_area_equal(self):
        # Adjusting to compare two equal rectangles
        square1 = Rectangle(name="Square1", width=5, height=5)  # Area = 25
        square2 = Rectangle(name="Square2", width=5, height=5)  # Area = 25
        result = square1.compare_area(square2)
        self.assertEqual(result, "Square1 and Square2 have the same area.")
