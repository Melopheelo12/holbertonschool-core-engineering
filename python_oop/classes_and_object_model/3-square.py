#!/usr/bin/env python3
class Square:
    def __init__(self, size=0):
        if not insistance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be > 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
