#!/usr/bin/python3
"""
function that creates an Object from a “JSON file
"""
import json


def load_from_json_file(filename):
    """yeep"""
    with open(filename, mode="r") as f:
        return json.load(f)
