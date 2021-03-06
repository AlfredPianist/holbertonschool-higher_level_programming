#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""1-rectangle

A Rectangle class with its private instance attributes width and height and its
setters and getters.
"""


class Rectangle:
    """A simple Rectangle class."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """The width of the rectangle.
        For the setter:
        Args:
            value (int): The width of the rectangle.
        Raises:
            TypeError: Width entered must be an integer.
            ValueError: Width entered must be a positive integer.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The height of the rectangle.
        For the setter:
        Args:
            value (int): The height of the rectangle.
        Raises:
            TypeError: Height entered must be an integer.
            ValueError: Height entered must be a positive integer.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
