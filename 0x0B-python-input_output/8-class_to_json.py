#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""6-load_from_json_file

This module has the function load_from_json_file which reads from a JSON file
and returns the object represented as JSON.
"""


def class_to_json(obj):
    """Returns the dictionar of an object to be serialized as JSON.
    Args:
        filename (str): The file name.
    Returns:
        obj: The object.
    """
    return obj.__dict__
