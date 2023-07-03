#!/usr/bin/python3
"""
rectagle class
"""


class Rectangle:
    """Represents a rectangle with a width, height"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the data."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @classmethod
    def square(cls, size=0):
        """makes a square"""
        return cls(size, size)

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

    def area(self):
        """
        method that returns the rectangle area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        method that returns the rectangle perimeter
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2

    def bigger_or_equal(rect_1, rect_2):
        """
        method that returns the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __str__(self):
        """print rectangle # """
        if not self.perimeter():
            return ""

        pattern = ["{}".format(self.print_symbol) *
                   self.width for _ in range(self.height)]
        return '\n'.join(pattern)

    def __repr__(self):
        """ print repr"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ print if deleted """
        Rectangle.number_of_instances -= 1
        print("{}".format("Bye rectangle..."))
