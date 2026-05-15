#!/usr/bin/env python3
"""Module defining an abstract Shape class and concrete shapes.

This module demonstrates the use of abstract base classes, concrete
subclasses, and duck typing in Python. It defines an abstract ``Shape``
class with two abstract methods, ``area`` and ``perimeter``, and two
concrete subclasses, ``Circle`` and ``Rectangle``. It also provides a
standalone function ``shape_info`` that relies on duck typing to print
information about any shape-like object.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class representing a geometric shape.

    Subclasses must implement the ``area`` and ``perimeter`` methods.
    """

    @abstractmethod
    def area(self):
        """Compute and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Compute and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete class representing a circle."""

    def __init__(self, radius):
        """Initialize a Circle with the given radius.

        Args:
            radius: The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize a Rectangle with the given width and height.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape-like object.

    This function uses duck typing: it does not check the type of the
    argument. It only requires that the object provide ``area`` and
    ``perimeter`` methods.

    Args:
        shape: Any object exposing ``area()`` and ``perimeter()`` methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
