#!/usr/bin/python3
"""square class"""
from models.rectangle import Rectangle


class Square(Rectangle):

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
        """"""
        if args:
            i = 0
            keys = ['id', 'width', 'height', 'x', 'y']
            for arg in args:
                setattr(self, keys[i], arg)
                i += 1

    def __str__(self):
        """print"""
        return ("[Rectangle] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.size))
