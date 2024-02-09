#!/usr/bin/python3
"""calculate island perimeter"""


def island_perimeter(grid: list) -> int:
    """get the island perimeter"""
    count = 0
    perimeter = 0
    if not isinstance(grid, list):
        return 0
    l_index = None
    c_index = None
    for i in grid:
        if not isinstance(i, list):
            return 0
        temp = i.count(1)
        if temp != 0:
            c_index = i.index(1)
            if temp == count and l_index is not None and c_index != l_index:
                perimeter += abs(c_index - l_index) * 2
            perimeter += abs(temp - count)
            perimeter += 2
            count = temp
            l_index = c_index
    perimeter += count
    return perimeter
