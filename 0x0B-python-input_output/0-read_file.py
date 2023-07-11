#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdou"""


def read_file(filename=""):
    """read and print file"""
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
