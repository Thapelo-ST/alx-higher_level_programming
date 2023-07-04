#!/usr/bin/python3
"""
    function/module that prints a matrix with a result of divided numbers
"""


def matrix_divided(matrix, div):
    if not all(isinstance(row, list) or not all(isinstance(row, list)) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not matrix:
        raise TypeError("matrix must not be empty")
    if not all(len(row) == len(matrix[0])for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return[[round(i / div, 2) for i in row]for row in matrix]
