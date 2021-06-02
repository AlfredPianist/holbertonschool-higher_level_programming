#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""2-is_same_class

This module has the function is_same_class which checks if a given object
is of the same class of a given class.
"""


def is_same_class(obj, a_class):
    """Returns True if obj is of the same class as a_class.
    Args:
        obj (:obj:): The object to be checked.
        a_class (:obj:): The class to be compared to the type of obj.
    Returns:
        bool: True if the type of obj is the same of a_class.
    """
    return type(obj) == a_class
