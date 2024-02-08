#!/usr/bin/python3
"""calculate island perimeter"""


def island_perimeter(grid: list) -> int:
    """get the island perimeter"""
    count = 0
    perimeter = 0
    for i in grid:
        temp = i.count(1)
        if temp != 0:
            perimeter += abs(temp - count)
            perimeter += 2
            count = temp
    perimeter += count
    return perimeter
