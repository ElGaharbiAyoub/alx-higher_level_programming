#!/usr/bin/python3
"""myInt class"""


class MyInt(int):
    """instance of MyInt"""

    def __init__(self, value):
        """initializes class"""
        self.value = value

    def __eq__(self, b):
        """equals change to not equals"""
        return self.value != b

    def __ne__(self, b):
        """reverses not equals to equals"""
        return self.value == b
