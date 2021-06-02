#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""9-student

This module creates class `Student` with public attributes first_name,
last_name and age, and a public method ``to_json`` that retrieves a dictionary
representation of a Student instance.
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

    def to_json(self):
        """Returns a dictionary representation of an instance of Student class.
        Returns:
            dict: The dictionary of a Student class instance.
        """
        return self.__dict__
