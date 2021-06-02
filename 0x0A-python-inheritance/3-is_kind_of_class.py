#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""3-is_kind_of_class

This module has the function is_same_class which checks if a given object
is an instance or is inherited from a given class.
"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance or is inherited from a_class.
    Args:
        obj (:obj:): The object to be checked.
        a_class (:obj:): The class to be compared.
    Returns:
        bool: True if the obj is an instance or is inherited from a_class.
    """
    return isinstance(obj, a_class)
