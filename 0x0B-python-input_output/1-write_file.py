#!/usr/bin/python3
"""
function that writes a string to a text file (UTF8) and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """writes a string"""
    with open(filename, mode='w') as f:
        f.write(text)
    return len(text)
