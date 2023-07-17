#!/usr/bin/python3
"""rectongle class"""
from models.base import Base


class Rectangle(Base):
    """represent rectangle class"""

    print_symbol = '#'

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # function thaf, att, value
    def validator(self, att, value):
        """validation of all setter """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(att))
        if (att == 'width' or att == 'height') and value <= 0:
            raise ValueError("{} must be > 0".format(att))
        if (att == 'x' or att == 'y') and value < 0:
            raise ValueError("{} must be >= 0".format(att))

    def update(self, *args, **kwargs):
        """updates attributes of rectongle """
        if args:
            i = 0
            keys = ['id', 'width', 'height', 'x', 'y']
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
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
        return dictionary

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        self.validator("width", value)
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        self.validator("height", value)
        self.__height = value

    @property
    def x(self):
        """get x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set x"""
        self.validator("x", value)
        self.__x = value

    @property
    def y(self):
        """get y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set y"""
        self.validator("y", value)
        self.__y = value

    def area(self):
        """return the area of rectongle"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        print('\n' * self.y, end="")
        pattern = [' ' * self.x + "{}".format(self.print_symbol) *
                   self.width for _ in range(self.height)]
        print('\n'.join(pattern))

    def __str__(self):
        """print"""
        return ("[Rectangle] ({}) {}/{} - {}/{}"
                .format(self.id, self.x, self.y, self.width, self.height))
