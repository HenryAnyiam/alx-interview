#!/usr/bin/python3
"""calculate island perimeter"""


def island_perimeter(grid: list) -> int:
    """get the island perimeter"""
    count = 0
    perimeter = 0
    if not isinstance(grid, list):
        return 0
    for i in grid:
        if not isinstance(i, list):
            return 0
        temp = i.count(1)
        if temp != 0:
            perimeter += abs(temp - count)
            perimeter += 2
            count = temp
    perimeter += count
    return perimeter
