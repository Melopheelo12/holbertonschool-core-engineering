#!/usr/bin/env python3
def uppercase(str):
    """print a string in uppercase"""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            char = chr(ord(char) - 32)
        print("{}".format(char), end="")
    print()
