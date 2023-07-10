#!/usr/bin/python3
"""
class BaseGeometry
"""


class BaseGeometry:
    """ class BaseGeometry"""

    def area(self):
        """ public instance method is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value for integer and positive"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
