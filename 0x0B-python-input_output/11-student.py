#!/usr/bin/python3
""" class Student"""


class Student:
    """heraab"""

    def __init__(self, first_name, last_name, age):
        """initializes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return __dict__"""
        if (isinstance(attrs, list) and
                all(isinstance(x, str) for x in attrs)):
            return ({x: y for x, y in self.__dict__.items() if x in attrs})
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        if (json):
            self.__dict__ = json
