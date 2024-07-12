#!/usr/bin/python3
canUnlockAll = __import__('0-lockboxes').canUnlockAll

"""Tests for lockboxes.py."""


boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

boxes = [[1, 4, 0], [2], [0, 4, 1], [3], [3, 6], [4, 1], [5, 6]]
print(canUnlockAll(boxes))

boxes = []
print(canUnlockAll(boxes))

boxes = [[], []]
print(canUnlockAll(boxes))

boxes = [[0], [1]]
print(canUnlockAll(boxes))

boxes = [[0], [1], [2]]
print(canUnlockAll(boxes))

print("\n Trying a thousand boxes")

athousand = []
for n in range(1, 1000):
    keys = []
    for i in range(1, 1000):
        keys.append(i)
    athousand.append(keys)
print(canUnlockAll(athousand))
