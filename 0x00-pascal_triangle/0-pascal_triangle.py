#!/usr/bin/python3
"""
Module with the pascals triangle generator
"""

def pascal_triangle(n):
    """generate a list of lists with pascal triangle"""
    triangle = []
    if n > 0:
        triangle = [[1]]
        n = n - 1
        for i in range(n):
            currVal = 0
            next = []
            length = len(triangle[-1])
            current = triangle[-1]
            for i in range(length):
                next.append(currVal + current[i])
                currVal = current[i]
            next.append(currVal + 0)
            triangle.append(next)
    return triangle
