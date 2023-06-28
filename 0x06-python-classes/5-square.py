#!/usr/bin/python3
"""
creates a square class object
"""


class Square:
    """
    Represents a square object.
    """

    def __init__(self, size=0):
        """
        Initializes an instance of the Square class.

        Args:
            size (int): Size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

    @property
    def size(self):
        """
        Getter property for the size of the square.

        Returns:
            int: Size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter property for the size of the square.

        Args:
            value (int): New size value for the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the area of the square based on its size.

        Returns:
            int: Area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints a representation of the square using '#' symbols.

        If the size is 0, it prints a newline character.
        """
        if self.size:
            for _ in range(self.size):
                print("#" * self.size)
        else:
            print()
