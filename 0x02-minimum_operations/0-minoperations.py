#!/usr/bin/env python3

"""
0-minoperations.py

An algorithm to find the minimum number of operations
to convert a string into another string

Problem: In a text file, there is a single character H.
Your text editor can execute only two operations in this
file: Copy All and Paste. Given a number n, write a method
that calculates the fewest number of operations needed to result
in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Returns the fewest number of operations needed
    to result in exactly n H characters in the file
    """
    if n <= 1:
        return 0
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n = n // i

    print(factors)
    return sum(factors)
