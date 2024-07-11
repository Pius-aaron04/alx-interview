#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min Ops for 4Hs")
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min Ops for 12Hs")
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 100
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
