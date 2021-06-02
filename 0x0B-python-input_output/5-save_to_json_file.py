#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""5-save_to_json_file

This module has the function save_to_json_file which writes a file with the
JSON representation of an object.
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes a file with the JSON representation of an object.
    Args:
        my_obj (:obj:): The object to be saved as a JSON file.
        filename (str): The file name.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
