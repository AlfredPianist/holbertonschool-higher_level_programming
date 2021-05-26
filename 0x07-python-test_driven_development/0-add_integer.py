#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""0-add_integer

Adds two integers.
"""


def add_integer(a, b=98):
    """Addition of two integers.
    Args:
        a (int): The first term.
        b (int): The second term.
    Returns:
        int: The sum of both terms.
    Raises:
        TypeError: both numbers must be integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return a + b
