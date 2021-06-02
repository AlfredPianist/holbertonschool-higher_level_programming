#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""100-append_after.py

This module includes the function `append_after` in which appends a line
after a string given by `search_string`
"""


def append_after(filename="", search_string="", new_string=""):
    """Appends a string `new_string` after finding an instance of
    `search_string`
    Args:
        filename (str): The file name.
        search_string (str): The string to be searched.
        new_string (str): The string to be appended after `search_string`.
    """
    with open(filename, 'r') as f:
        content = f.readlines()

    idx_insert = []
    for idx, line in enumerate(content):
        if search_string in line:
            idx_insert.append(idx + 1)
    i = 0
    while i < len(idx_insert):
        content.insert(idx_insert[i], new_string)
        for j in range(i + 1, len(idx_insert)):
            idx_insert[j] += 1
        i += 1
    content = "".join(content)

    with open(filename, 'w') as f:
        f.write(content)
