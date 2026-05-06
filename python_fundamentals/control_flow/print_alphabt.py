#!/usr/bin/env python 3
for letter in range(ord('a'), ord('z') + 1):
    if char(letter) != 'q' and char(letter) != 'e':
        print("{}".format(char(letter)), end="")
