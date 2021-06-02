#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""3-to_json_string

This module has the function to_json_string which returns the JSON
representation of an object.
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object as a string.
    Args:
        my_obj (:obj:): The object to be dumped as JSON.
    Returns:
        str: The JSON string of the object.
    """
    return json.dumps(my_obj)
