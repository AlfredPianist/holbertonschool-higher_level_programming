#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""1-my_list

This module creates a class `MyList` inheriting from the class `list` and has a
public method that prints the list sorted.
"""


class MyList(list):
    """A class inheriting from the `list` class."""

    def print_sorted(self):
        """Prints the list sorted."""
        print(sorted(self))
