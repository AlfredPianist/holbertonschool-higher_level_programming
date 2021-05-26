#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""101-lazy_matrix_mul.py

Returns a matrix with the result of the product of two matrices, using NumPy.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Returns a matrix with the result of the product of two matrices
    usign NumPy.
    Args:
        m_a (list of list of int or float): The first matrix.
        m_b (list of list of int or float): The second matrix.
    Returns:
        :obj:`array`: The matrix product of m_a and m_b.
    """
    return numpy.matmul(m_a, m_b)
