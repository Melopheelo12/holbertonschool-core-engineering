#!/usr/bin/env python3
"""Module that reads a UTF8 text file and prints its content."""


def read_file(filename=""):
    """Read a UTF8 text file and print its content to stdout.

    Args:
        filename (str): The path to the file to read. Defaults to "".
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
