#!/usr/bin/env python3
"""Module for Rectangle"""
BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """instantiate a rectangle"""
        self.integer_validation("width", width)
        self.integer_validation("height", height)
        self.__width = width
        self.__height = height
