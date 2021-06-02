#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""101-add_attribute

This module contains a function that adds a new attribute to an object
if possible.
"""


def add_attribute(obj, name, value):
    """Function that adds a new attribute to an object if possible.
    Args:
        obj (:obj:): The object to be added a new attribute.
        name (str): The name of the new attribute.
        value (:obj:): The value of the new attribute.
    Raises:
        TypeError: Attribute can't be added.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
