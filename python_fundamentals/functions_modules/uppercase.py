#!/usr/bin/env python3
def uppercase(str):
    for c in str:
        if ord('97') <= ord(c) <= ord('122'):
            c = chr(ord(char) - 32)
        print("{}".format(c), end="")
    print()
