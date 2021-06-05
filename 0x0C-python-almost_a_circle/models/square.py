#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""square module.

This is the Square class inherited from the Rectangle class, ...
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class inherited from Rectangle class."""

    def __init__(self, size, x=0, y=0, id=None):
        """The class constructor.
        Args:
            size (int): The size of the square.
            x (int): The x coordinate offset when displaying the square.
            y (int): The y coordinate offset when displaying the square.
            id (int): The id of the current square instance.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """The size of the square.
        For the setter:
        Args:
            value (int): The size of the rectangle.
        """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """String representation of a square instance.
        Returns:
            str: The string representation of a square.
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Updates the square instance"""
        if args:
            arg_order = ["id", "size", "x", "y"]
            for index, arg in enumerate(args):
                setattr(self, arg_order[index], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation of a square instance.
        Returns:
            dict: The dictionary representation of a square.
        """
        dict_contents = ["id", "size", "x", "y"]
        new_dict = {}
        for key in dict_contents:
            new_dict[key] = getattr(self, key)
        return new_dict
