#!/usr/bin/python3
"""Module contains: class Square """


class Square():
    """
    Square: defines a square.
    Attributes:
    size (no type or value identification): size of square.
    Method:
    __init__ : init of size attributefor each instance.
    """

    def __init__(self, size):

        """ Initialization of attributes for instances
        Args:
        size (no type): size of the square.
        """
        self.__size = size
