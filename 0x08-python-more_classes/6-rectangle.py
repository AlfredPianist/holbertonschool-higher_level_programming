#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""6-rectangle

A Rectangle class with a public class attribute "number_of_instances" keeping
track of the instances created, its private instance attributes width and
height and its setters and getters, and area and perimeter as public methods
as well as a string representation of itself using the '#' character, a
representation (Rectangle(width, height)) to be evaluated by eval(), and a
message printed when a Rectangle instance is deleted.
"""


class Rectangle:
    """A simple Rectangle class.

    Attributes:
        number_of_instances (int): The number of instances of the Rectangle
                                   class created.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """String representation of the rectangle using the '#' character."""
        string = ""
        if not (self.__width == 0 or self.__height == 0):
            for i in range(self.__height):
                string += "#" * self.__width
                if i < self.__height - 1:
                    string += "\n"
        return string

    def __repr__(self):
        """Representation of a Rectangle instance to be parsed by eval() as
        Rectangle(width, height).
        """
        return "Rectangle({}, {})".format(str(self.__width),
                                          str(self.__height))

    def __del__(self):
        """Calls the garbage collector, prints a message when an instance
        of Rectangle is deleted and subtracts an instance from the
        number_of_instances class public attribute.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def area(self):
        """Calculates the area of a rectangle.
        Returns:
            int: The area of a rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a rectangle.
        Returns:
            int: The perimeter of a rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
