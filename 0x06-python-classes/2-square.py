#!/usr/bin/python3
""" 2-square: class Square """


class Square():
    """
    Square: defines a square.
    Attributes:
    size (no type or value identification):
    Method:
    __init__ : init of size attribute for each instance.
    """

    def __init__(self, size=0):

        """ Initialization of attributes for instances
        Args:
        size (int): size of the square.
        """
        if (isinstance(size, int)):
            self.__size = size
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
