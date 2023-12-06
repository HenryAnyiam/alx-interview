#!/usr/bin/python3
"""LockBoxes"""


def canUnlockAll(boxes):
    """Function to check if all boxes can be unlocked
       Boxes is a list of lists
    """

    unlocked = {0}
    length = len(boxes)
    for index, value in enumerate(boxes):
        if not value:
            continue
        for key in value:
            if (key < length) and (key not in unlocked) and (key != index):
                unlocked.add(key)
    return len(unlocked) != length
