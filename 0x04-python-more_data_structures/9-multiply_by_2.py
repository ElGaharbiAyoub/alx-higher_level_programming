#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for key, val in a_dictionary.items():
        new_dict[key] = val * 2
    return new_dict
