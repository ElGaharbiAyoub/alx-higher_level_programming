#!/usr/bin/python3
"""adds a new attribute to an object if its possible"""


def add_attribute(obj, attribute, value):
    """adds new attribute"""
    setattr(obj, attribute, value)
    if not hasattr(obj, attribute) or getattr(obj, attribute) != value:
        raise TypeError("can't add new attribute")
