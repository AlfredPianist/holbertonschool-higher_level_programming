#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for i, row in enumerate(new_matrix):
        new_matrix[i] = list(map(lambda x: x ** 2, row))
    return new_matrix
