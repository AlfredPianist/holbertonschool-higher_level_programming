#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""2-matrix_divided

Divides a matrix of numbers with a given divisor.
"""


def matrix_divided(matrix, div):
    """Division of matrix by div.
    Args:
        matrix (list of list of int or float): The matrix.
        div (int or float): The divisor.
    Returns:
        list of list of float: The matrix divided by div.
    Raises:
        TypeError: all numbers in matrix and divisor must be of type int or
                   float.
        TypeError: all rows in matrix must have the same size.
        ZeroDivisionError: divisor must not be zero (division by zero).
    """
    if not(isinstance(matrix, list) and len(matrix) > 0 and
           all(isinstance(row, list) and len(row) > 0 for row in matrix) and
           all(isinstance(val, (int, float)) for row in matrix
               for val in row)):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if not all(len(matrix[0]) == len(row) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(val/div, 2) for val in row] for row in matrix]
