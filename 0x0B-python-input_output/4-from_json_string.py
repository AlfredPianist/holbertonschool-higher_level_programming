#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""4-from_json_string

This module has the function from_json_string which returns an object
represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string.
    Args:
        my_str (str): The JSON string.
    Returns:
        obj: The object saved as a JSON string.
    """
    return json.loads(my_str)
