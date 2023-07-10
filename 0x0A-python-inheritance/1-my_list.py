#!/usr/bin/python3
"""my class mylist"""


class MyList(list):
    """class that inherits from list"""

    def print_sorted(self):
        print(sorted(self))
