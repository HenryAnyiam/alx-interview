#!/usr/bin/python3
"""Lockboxes interview question"""


def canUnlockAll(boxes):
    """function to unluck boxes"""
    if not isinstance(boxes, list):
        return False
    length = len(boxes)
    if length <= 1:
        return True
    locked = length - 1
    keys = set(boxes[0]) if isinstance(boxes[0], list) else None
    keys.add(0)
    unlock = True
    all_box = [i for i in range(length)]
    while unlock:
        hold = keys
        for i in keys:
            try:
                hold = hold.union(set(boxes[i]))
            except (IndexError, TypeError) as e:
                pass
        if len(hold) > len(keys):
            keys = hold
        else:
            unlock = False
    if keys != set(all_box):
        return False
    return True
