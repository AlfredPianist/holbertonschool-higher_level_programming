#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""6-load_from_json_file

This module has the function load_from_json_file which reads from a JSON file
and returns the object represented as JSON.
"""
import json


def load_from_json_file(filename):
    """Returns an object from a JSON file.
    Args:
        filename (str): The file name.
    Returns:
        obj: The object.
    """
    with open(filename, 'r') as f:
        return json.load(f)
