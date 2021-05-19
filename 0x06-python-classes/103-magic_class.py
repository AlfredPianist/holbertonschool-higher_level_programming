#!/usr/bin/python3
"""103-magic-class - A simple Circle class."""
import math


class MagicClass:
    """MagicClass. A Circle Class."""
    def __init__(self, radius=0):
        """Initialization of MagicClass object with its radius."""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates the area of a Circle object."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circunference of a Circle object."""
        return 2 * math.pi * self.__radius
