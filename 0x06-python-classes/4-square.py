#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""4-square
A Square class with size as its only private attribute (and its
getter and setter methods), and area as a method.
"""


class Square:
    """A simple Square class.

    Attributes:
            __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initialization of Square object with size.
        """
        self.size = size

    @property
    def size(self):
        """The size of the square.
        For the setter:
        Args:
            value (int): The size of the square.
        Raises:
            TypeError: Size entered must be an integer.
            ValueError: Size entered must be a positive integer.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of a square.
        Returns:
            The area of a square.
        """
        return (self.__size ** 2)
