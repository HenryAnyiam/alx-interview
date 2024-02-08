#!/usr/bin/python3
"""calculate island perimeter"""


def island_perimeter(grid: list) -> int:
    """get the island perimeter"""
    count = 0
    perimeter = 0
    for i in grid:
        temp = i.count(1)
        if count != 0 and temp == 0:
            perimeter += count
            break
        elif temp != 0:
            perimeter += abs(temp - count)
            perimeter += 2
            count = temp
    return perimeter
