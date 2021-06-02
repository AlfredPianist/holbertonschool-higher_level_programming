#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""4-inherits_from

This module has the function inherits_from which checks if a given object
is a subclass of a given class.
"""


def inherits_from(obj, a_class):
    """Returns True if obj is a subclass of a_class.
    Args:
        obj (:obj:): The object to be checked.
        a_class (:obj:): The class to be compared.
    Returns:
        bool: True if the obj is a subclass of a_class.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
