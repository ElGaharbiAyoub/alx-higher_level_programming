#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    elem1 = tuple_a or (0, 0)
    elem2 = tuple_b or (0, 0)
    if len(tuple_a) == 1:
        elem1 = (tuple_a[0], 0)
    if len(tuple_b) == 1:
        elem2 = (tuple_b[0], 0)
    elem3 = (elem1[0] + elem2[0], elem1[1] + elem2[1])
    return elem3
