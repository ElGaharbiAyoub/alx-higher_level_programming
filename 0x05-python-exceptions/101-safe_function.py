#!/usr/bin/python3
from sys import stderr

def safe_function(fct, *args):
    try:
        result = fct(*args)
    except Exception as inst:
        print("Exception: {}".format(inst), file=stderr)
        return (None)
    return (result)
