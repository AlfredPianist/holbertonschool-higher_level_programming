#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""7-base_geometry

This module creates a class `BaseGeometry` with access to methods ``area`` and
``integer_validator.
"""


class BaseGeometry():
    """BaseGeometry class with methods ``area`` and ``integer_validator``."""

    def area(self):
        """A method with a sole exception when called."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if a given value is a positive number.
        Args:
            name (str): The name of the value.
            value (int): The actual value to be validated.
        Raises:
            TypeError: Value must be an enteger.
            ValueError: Value must be a positive integer.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
