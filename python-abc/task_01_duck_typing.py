#!/usr/bin/env python3
"""
Import the necessary components from the abc module
"""

from abc import ABC, abstractmethod
import math

"""
Define the Shape class, ensuring it inherits from ABC to mark it as abstract
"""


class Shape(ABC):
    """
    Abstract class Shape that requires subclasses to implement
    the area and perimeter methods.
    """

    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.
        This method should be implemented by subclasses.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.
        This method should be implemented by subclasses.
        """
        pass


class Circle(Shape):
    """
    Circle is a subclass of Shape that represents a circle.
    """
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle is a subclass of Shape that represents a rectangle.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
