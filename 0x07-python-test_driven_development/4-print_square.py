#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""4-print_square

Prints a square of size 'size' filled with the '#' character.
"""


def print_square(size):
    """Prints a square of size 'size' filled with the '#' character.
    Args:
        size (int): The size of the square.
    Raises:
        TypeError: size must be of type int.
        ValueError: size must be >= 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
