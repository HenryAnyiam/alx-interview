#!/usr/bin/python3
"""UTF-8 Validation"""


def check_range(start, end, arr):
    """check that the characters between start
    and end fall between 128 and 191"""
    while start < end:
        if not (128 >= arr[start] <= 191):
            return False
        start += 1
    return True


def validUTF8(data):
    """validate that datais a valid utf-8"""
    length = len(data) if data else 0
    i = 0

    while i < length:
        if data[i] > 255:
            return False

        if data[i] <= 127:
            i += 1
        elif 193 <= data[i] <= 223:
            if ((i + 2) >= length or not check_range((i + 1), (i + 2), data)):
                return False
            i += 2
        elif 224 <= data[i] <= 239:
            if ((i + 3) >= length or not check_range((i + 1), (i + 3), data)):
                return False
            i += 3
        elif 240 <= data[i] <= 247:
            if ((i + 4) >= length or not check_range((i + 1), (i + 4), data)):
                return False
            i += 4
        else:
            return False
    return True
