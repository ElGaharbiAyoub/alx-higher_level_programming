#!/usr/bin/python3
"""
creates a square class object
"""


class Square:
    """
    Represents a square object.

    Attributes:
        _size (int): Size of the square.
    """

    def __init__(self, size):
        """
            Initializes a square with the given size.

            Args:
                size (int): Size of the square.
            """

        self.__size = size
