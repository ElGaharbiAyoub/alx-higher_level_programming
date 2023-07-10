#!/usr/bin/python3
"""
function that returns True if the object is an instance of, or if the object
is an instance of a classthat inherited from, the specified class;
otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """returns subclass"""
    return isinstance(obj, a_class)
