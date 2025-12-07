#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return map(lambda i : map(lambda j : j*j, i), matrix)
