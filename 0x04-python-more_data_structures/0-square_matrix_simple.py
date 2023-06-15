#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    calc = [[0 for i in row] for row in matrix]

    for w in range(len(matrix)):
        for j in range(len(matrix[w])):
            calc[w][j] = matrix[w][j] ** 2
    return calc
