#!/usr/bin/python3
"""
rectagle class
"""


class Rectangle:
    """Represents a rectangle with a width, height"""

    def __init__(self, width=0, height=0):
        """Initializes the data."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """return width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width value"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """return height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height value"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
