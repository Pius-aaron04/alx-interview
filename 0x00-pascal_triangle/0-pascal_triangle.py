#!/usr/bin/python3

"""
Pascal triangle
"""


def pascal_triangle(n):
    """
    Generates a 2D array of n rows representing a Pascal triangle

    return: empty list if n <= 0 else list of n lists
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        if i == 1:
            triangle.append([1, 1])
        else:
            prev = triangle[i - 1]
            new = []
            for j in range(len(prev)):
                if j == 0 and j < len(prev) - 1:
                    new.append(prev[j])
                    new.append(prev[j] + prev[j + 1])
                elif j > 0 and j < len(prev) - 1:
                    new.append(prev[j] + prev[j + 1])
                else:
                    new.append(prev[j])
            triangle.append(new)

    return triangle
