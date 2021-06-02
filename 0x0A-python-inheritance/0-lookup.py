#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""0-lookup

This module has the function lookup which checks all the attributes
and methods of an object
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object.
    Args:
        obj (:obj:): The object to be checked.
    Returns:
        list: List of available attributes of object `obj`.
    """
    return dir(obj)
