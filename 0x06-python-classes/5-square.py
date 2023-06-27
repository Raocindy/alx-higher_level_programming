#!/usr/bin/python3
"""Square class defination"""


class Square:
    """Square class body"""

    def __init__(self, size):
        """Square contructor
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Square setter and getter for _size."""
        return (self._size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        """Return th area of a square."""
        return (self._size * self._size)

    def my_print(self):
        """Print stdout the square with the character"""
        for i in range(0, self._size):
            [print("#", end="") for j in range(self._size)]
            print("")
        if self._size == 0:
            print("")
