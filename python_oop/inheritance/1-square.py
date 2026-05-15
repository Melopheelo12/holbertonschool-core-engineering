#!/usr/bin/env python3
"""Module defining a Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class, a specialized Rectangle where width equals height."""

    def __init__(self, size):
        """Initialize a Square with the given size.

        Args:
            size: The size of the square (must be a positive integer).
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size