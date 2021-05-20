#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""9-rectangle

A Rectangle class with public class attributes "number_of_instances" keeping
track of the instances created and "print_symbol" modifying its print symbol,
its private instance attributes width and height and its setters and getters,
area and perimeter as public methods, a static method bigger_or_equal
calculating the biggest area of two rectangles, a class method square returning
a new instance of Rectangle with the same dimensions of width and height, as
well as a string representation of itself using the '#' character, a
representation (Rectangle(width, height)) to be evaluated by eval(), and a
message printed when a Rectangle instance is deleted.
"""


class Rectangle:
    """A simple Rectangle class.

    Attributes:
        number_of_instances (int): The number of instances of the Rectangle
                                   class created.
        print_symbol (:obj:): The symbol to use for the Rectangle's instance
                              string representation.
    """

    number_of_instances = 0
    print_symbol = '#'

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
                string += str(self.print_symbol) * self.__width
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the rectangle with the biggest area.
        If both areas are equal, returns the first rectangle.
        Args:
            rect_1 (:obj:`Rectangle`): The first rectangle.
            rect_2 (:obj:`Rectangle`): The second rectangle.
        Returns:
            :obj:`Rectangle`: The rectangle with the biggest area.
        Raises:
            TypeError: Both rectangles must be instances of Rectangle.

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() >= rect_2.area()):
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance in which its width and area
        are the same (a square).
        """
        return cls(size, size)
