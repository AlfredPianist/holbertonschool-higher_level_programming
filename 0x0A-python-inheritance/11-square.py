#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""11-square

This module creates class `Square` inherited from `Rectangle` with private
attribute size, and the ``area`` and ``__str__`` methods.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A simple Square class."""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        """Returns a description of the square instance."""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

    def area(self):
        """Calculates the area of the square instance.
        Returns:
            int: The square area.
        """
        return self.__size ** 2
