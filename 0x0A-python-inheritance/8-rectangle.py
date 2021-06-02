#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""8-rectangle

This module creates class `Rectangle` inherited from `BaseGeometry` with two
private attributes width and height.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A simple Rectangle class."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
