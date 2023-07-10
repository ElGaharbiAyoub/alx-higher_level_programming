#!/usr/bin/python3
"""
the object is an instance of, or if the object
is an instance of a classthat inherited from
"""


def inherits_from(obj, a_class):
    """returns subclass"""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
