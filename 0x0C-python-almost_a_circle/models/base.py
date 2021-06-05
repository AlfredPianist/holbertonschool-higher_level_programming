#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""base module.

This is the Base class from which the other classes will be based. It only has
one class attribute __nb_objects serving as a counter of instances, and the
class constructor.
"""


class Base():
    """A Base class working as superclass of Rectangle."""
    __nb_objects = 0

    def __init__(self, id=None):
        """The class constructor.
        Args:
            id (int): The id of the instance. If id is provided, the
                      instance's id will be the one provided. Otherwise, the
                      private class astribute's __nb_objects one will be
                      assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
