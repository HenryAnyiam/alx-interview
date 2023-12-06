#!/usr/bin/python3

canUnlockAll = __import__('0-lockboxe').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[4], [2, 7], [0, 4, 1], [5, 6, 2], [3], [4, 1], [1, 4, 6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2, 4], [0, 4, 1], [3, 1], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
print(canUnlockAll([[1], "", [], [1]]))
