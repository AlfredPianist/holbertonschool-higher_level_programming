#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""5-text_indentation

Prints a text with two newline characters after '?', '.' or ':' characters.
"""


def text_indentation(text):
    """Prints a text with two newline characters after '?', '.' or ':'
    characters.
    Args:
        text (str): The text to be indented.
    Raises:
        TypeError: text must be of type string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    begin_slice, end_slice = 0, 0
    begin_slice_found, end_slice_found = False, False
    last_line = False

    for i, c in enumerate(text):
        if (c not in " \t" and begin_slice_found is False):
            begin_slice = i
            begin_slice_found = True
        if (begin_slice_found is True):
            if (c in " \t" and end_slice_found is False) or (c in ".:?"):
                end_slice = i
                end_slice_found = True
            if (c not in " \t\n\r"):
                end_slice = i
                end_slice_found = False
            if (i == len(text) - 1):
                print(text[begin_slice:end_slice + 1])
                last_line = True
            if (c in ".:?\n\r") and last_line is False:
                if (text[end_slice] in " \t\n\r"):
                    print(text[begin_slice:end_slice])
                else:
                    print(text[begin_slice:end_slice + 1])
                begin_slice_found, end_slice_found = False, False
            if (c in ".:?"):
                print("")
