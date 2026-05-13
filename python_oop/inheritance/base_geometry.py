#!/usr/bin/env python3
"""Defines a base class for geometric shapes."""


class BaseGeometry:
    """Represents a foundation for geometric shape classes.

    Provides shared behavior that subclasses can build upon,
    including a common interface for computing area and a
    helper for validating integer parameters.
    """

    def area(self):
        """Compute the area of the shape.

        Not implemented at the base level because each shape
        calculates its area differently. Subclasses are expected
        to override this method.

        Raises:
            Exception: always, with the message
                "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a strictly positive integer.

        Args:
            name (str): the label used in error messages.
            value: the value to validate.

        Raises:
            TypeError: if value is not an int (or is a bool).
            ValueError: if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
