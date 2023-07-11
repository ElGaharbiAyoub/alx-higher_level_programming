#!/usr/bin/python3
"""square class"""

Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """creates square"""

    def __init__(self, size):
        """initializes rectangle"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
