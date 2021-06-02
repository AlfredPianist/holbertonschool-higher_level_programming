#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""0-read_file

This module has the function read_file which reads the content from a file.
"""


def read_file(filename=""):
    """Reads and prints the content from a file.
    Args:
        filename (str): The file name to be opened and read.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
