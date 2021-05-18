#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""3-square
A Square class with size as its only private attribute,
and area as its only method.
"""


class Square:
    """A simple Square class.

    Attributes:
            __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initialization of Square object with size.
        Args:
            size (int): The size of the square.
        Raises:
            TypeError: Size entered must be an integer.
            ValueError: Size entered must be a positive integer.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of a square.
        Returns:
            The area of a square.
        """
        return (self.__size ** 2)
