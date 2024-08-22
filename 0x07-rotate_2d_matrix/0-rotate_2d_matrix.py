#!/usr/bin/python3

"""2D Matrix rotation.
"""


def rotate_2d_matrix(matrix):
    """Clockwise roatation of matrix"""
    matrix_size = len(matrix)

    # Transposing matrix
    for i in range(matrix_size):
        for j in range(i, matrix_size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # rows reversal
    for i in range(matrix_size):
        for j, value in enumerate(matrix[i][::-1]):
            matrix[i][j] = value
