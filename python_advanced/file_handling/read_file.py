#!/usr/bin/env python3
""" Module that read UTF8 text"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
