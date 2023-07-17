#!/usr/bin/python3
"""square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """represent square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get size"""
        return self.width

    @size.setter
    def size(self, value):
        """set size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates attributes of square"""
        if args:
            i = 0
            keys = ['id', 'size', 'x', 'y']
            for arg in args:
                setattr(self, keys[i], arg)
                i += 1
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary"""
        dictionary = {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
        return dictionary

    def __str__(self):
        """print"""
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))
