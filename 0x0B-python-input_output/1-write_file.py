#!/usr/bin/python3
"""
function that writes a string to a text file (UTF8) and
returns the number of characters written
"""


def write_file(filename="", text=""):
    """writes a string"""
    line = 0
    with open(filename, mode='w', encoding='utf-8') as f:
        for line in f:
            line += 1
    return line
