#!usr/bin/python3
"""Rotate a 2d matrix"""


def rotate_2d_matrix(matrix):
    """rotate a n X n matrix 90 degrees"""
    matrix_len = len(matrix)

    # Iterating through the rows and cols and swapping them
    for i in range(matrix_len):
        for j in range(i, matrix_len):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_len):
        matrix[i] = matrix[i][::-1]
