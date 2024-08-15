#!/usr/bin/python3

"""2D Matrix rotation.
"""


def rotate_2d_matrix(matrix):
    """Clockwise roatation of matrix"""
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        for j, x in enumerate(matrix[i][::-1]):
            matrix[i][j] = x
