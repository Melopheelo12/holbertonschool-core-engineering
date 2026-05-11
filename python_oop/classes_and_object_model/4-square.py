#!/usr/bin/env python3
class Square:
    def __init__(self, size=0):
        self.__size = 0
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.stter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("Size must be an integer")
        if value < 0:
            raise ValueError("Value must be > 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
