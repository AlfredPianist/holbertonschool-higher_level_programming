#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""101-square
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

    def __lt__(self, other):
        """Compares if self area is less than other area
        Returns:
            True if self area less than other area, False otherwise
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Compares if self area is less or equal than other area
        Returns:
            True if self area less or equal than other area, False otherwise
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compares if self area is greater than other area
        Returns:
            True if self area greater than other area, False otherwise
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Compares if self area is greater or equal than other area
        Returns:
            True if self area greater or equal than other area, False otherwise
        """
        return self.area() >= other.area()

    def __eq__(self, other):
        """Compares if self area is equal than other area
        Returns:
            True if self area equal than other area, False otherwise
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Compares if self area is different than other other area
        Returns:
            True if self area different than other area, False otherwise
        """
        return self.area() != other.area()

    def area(self):
        """Calculates the area of a square.
        Returns:
            The area of a square.
        """
        return (self.__size ** 2)
