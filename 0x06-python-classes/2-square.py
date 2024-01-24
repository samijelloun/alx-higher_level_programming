#!/usr/bin/python3
"""A module that defines a square"""


class Square:
    """A class that represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initializing this square class.

        Args:
            size (int): Represents the size of the square.
                Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
