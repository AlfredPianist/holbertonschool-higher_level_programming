#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""1-write_file

This module has the function write_file which writes a text to a file.
"""


def write_file(filename="", text=""):
    """Writes some text to a file.
    Args:
        filename (str): The file name to be opened and read.
        text (str): The text to be written.
    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
