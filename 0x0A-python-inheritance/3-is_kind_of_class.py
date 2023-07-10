#!/usr/bin/python3
"""
function that returns True if the object is an instance of, or if the object
is an instance of a classthat inherited from, the specified class;
otherwise False.
"""


def inherits_from(obj, a_class):
    """returns subclass yes"""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
