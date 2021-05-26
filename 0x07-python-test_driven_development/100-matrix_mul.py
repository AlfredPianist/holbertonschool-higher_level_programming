#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""100-matrix_mul.py

Returns a matrix with the result of the product of two matrices.
"""


def matrix_mul(m_a, m_b):
    """Returns a matrix with the result of the product of two matrices.
    Args:
        m_a (list of list of int or float): The first matrix.
        m_b (list of list of int or float): The second matrix.
    Returns:
        list of list of float: The matrix product of m_a and m_b.
    Raises:
        TypeError: all numbers in matrix and divisor must be of type int or
                   float.
        TypeError: all rows in matrix must have the same size.
    """
    if not(isinstance(m_a, list)):
        raise TypeError("m_a must be a list")
    if not(isinstance(m_b, list)):
        raise TypeError("m_b must be a list")

    if not(all(isinstance(row, list) for row in m_a)):
        raise TypeError("m_a must be a list of lists")
    if not(all(isinstance(row, list) for row in m_b)):
        raise TypeError("m_b must be a list of lists")

    if not(len(m_a) > 0 and
           all(isinstance(row, list) and len(row) > 0 for row in m_a)):
        raise ValueError("m_a can't be empty")
    if not(len(m_b) > 0 and
           all(isinstance(row, list) and len(row) > 0 for row in m_b)):
        raise ValueError("m_b can't be empty")

    if not(all(isinstance(val, (int, float)) for row in m_a for val in row)):
        raise TypeError("m_a should contain only integers or floats")
    if not(all(isinstance(val, (int, float)) for row in m_b for val in row)):
        raise TypeError("m_b should contain only integers or floats")

    if not(all(len(m_a[0]) == len(row) for row in m_a)):
        raise TypeError("each row of m_a must be of the same size")
    if not(all(len(m_b[0]) == len(row) for row in m_b)):
        raise TypeError("each row of m_b must be of the same size")

    if not(len(m_a[0]) == len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")

    return [[round(sum(a * b for a, b in zip(a_row, b_col)), 4)
             for b_col in zip(*m_b)] for a_row in m_a]
