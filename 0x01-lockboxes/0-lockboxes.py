#!/usr/bin/python3
"""
Technical interview task: Lockboxes.
Defines a function which determines if all boxes in a list can ba unlocked.
Where a box contain key(s) to other box(es) with the first box in the list
open.
"""


def openBox(boxes, box, unlockedBoxes):
    """
    Opens indiviual boxes via key
    and recursively calls itself to open other boxes.
    """
    for key in box:
        if key in unlockedBoxes:
            continue

        if key < len(boxes):
            unlockedBoxes.add(key)
            openBox(boxes, boxes[key], unlockedBoxes)
        openBox(boxes, boxes[key], unlockedBoxes)

    return


def canUnlockAll(boxes):
    """
    Checks if all boxes can be unlocked.
    """

    if not boxes:
        return True

    unlockedBoxes = {0}

    # start of a recursive call

    openBox(boxes, boxes[0], unlockedBoxes)

    # end of the call

    if len(unlockedBoxes) == len(boxes):
        return True
    return False
