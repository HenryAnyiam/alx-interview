#!/usr/bin/python3
"""Lockboxes interview question"""


def canUnlockAll(boxes):
    """function to unluck boxes"""
    if not isinstance(boxes, list):
        return False
    length = len(boxes)
    if length <= 1:
        return True
    keys = set(boxes[0]) if isinstance(boxes[0], list) else None
    keys.add(0)
    unlock = True
    unlocked = keys
    expected_keys = [i for i in range(length)]
    while unlock:
        hold = set()
        for i in keys:
            try:
                hold = hold.union(set(boxes[i]))
            except (IndexError, TypeError) as e:
                pass
        if not hold.issubset(unlocked):
            keys = hold
            unlocked = unlocked.union(keys)
        else:
            unlock = False
    return set(expected_keys).issubset(unlocked)
