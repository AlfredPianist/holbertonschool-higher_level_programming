#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""rectangle module.

This is the Rectangle class inherited from the Base class, with private
attributes width, height and x and y as offsets for printing the rectangle,
each with its getters and setters, and public methods area, display and update.
"""
from models.base import Base


class Rectangle(Base):
    """A Rectangle class inherited from Base class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The class constructor.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x coordinate offset when displaying the rectangle.
            y (int): The y coordinate offset when displaying the rectangle.
            id (int): The id of the current rectangle instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """The x coordinate offset for printing the rectangle.
        For the setter:
        Args:
            value (int): The x coordinate of the rectangle.
        Raises:
            TypeError: x value entered must be an integer.
            ValueError: x value entered must be a positive integer including 0.
        """
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """The y coordinate offset for printing the rectangle.
        For the setter:
        Args:
            value (int): The y coordinate of the rectangle.
        Raises:
            TypeError: y value entered must be an integer.
            ValueError: y value entered must be a positive integer including 0.
        """
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        """String representation of a rectangle instance.
        Returns:
            str: The string representation of a rectangle.
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height)

    def area(self):
        """Calculates the area of a rectangle.
        Returns:
            int: The area of a rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the rectangle instance."""
        print("".join("\n" for y in range(self.y)), end='')
        for row in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def update(self, *args, **kwargs):
        """Updates the rectangle instance"""
        if args:
            arg_order = ["id", "width", "height", "x", "y"]
            for index, arg in enumerate(args):
                setattr(self, arg_order[index], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation of a rectangle instance.
        Returns:
            dict: The dictionary representation of a rectangle.
        """
        dict_contents = ["id", "width", "height", "x", "y"]
        new_dict = {}
        for key in dict_contents:
            new_dict[key] = getattr(self, key)
        return new_dict
