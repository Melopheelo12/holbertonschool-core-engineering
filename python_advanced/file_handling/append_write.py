#!/usr/bin/env python3
"""Module that appends a string to the end of a text file."""


def append_write(filename="", text=""):
    """Append a string to the end of a UTF8 text file.

    Creates the file if it does not exist.

    Args:
        filename (str): The path to the file. Defaults to "".
        text (str): The string to append. Defaults to "".

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
