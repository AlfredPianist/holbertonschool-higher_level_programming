#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""100-my_int

This module creates class `MyInt` inherited from int with swapped
__eq__ and __ne__ magic methods.
"""


class MyInt(int):
    """A custom int class with swapped __eq__ and __ne__ magic methods."""

    def __eq__(self, other):
        """== is now !="""
        return super().__ne__(other)

    def __ne__(self, other):
        """!= is now =="""
        return super().__eq__(other)
