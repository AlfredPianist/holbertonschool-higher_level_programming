#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""5-base_geometry

This module creates a class `BaseGeometry` with access to method ``area``.
"""


class BaseGeometry():
    """BaseGeometry class with method ``area``"""

    def area(self):
        """A method with a sole exception when called."""
        raise Exception("area() is not implemented")
