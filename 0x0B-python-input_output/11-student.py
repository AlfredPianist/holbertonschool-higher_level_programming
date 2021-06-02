#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""11-student

This module creates class `Student` with public attributes first_name,
last_name and age, and two public methods: ``to_json`` that retrieves a
dictionary representation of a Student instance and ``reload_from_json``` which
updates all attributes from a JSON file.
"""


class Student():
    """A simple Student class.
    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of an instance of Student class.
        Returns:
            dict: The dictionary of a Student class instance filtered if attrs
                  exist.
        """
        if attrs is None:
            return self.__dict__
        dic = {}
        for attr in attrs:
            if hasattr(self, attr):
                dic[attr] = getattr(self, attr)
        return dic

    def reload_from_json(self, json):
        """Updates all attributes from a JSON file."""
        for key, value in json.items():
            setattr(self, key, value)
