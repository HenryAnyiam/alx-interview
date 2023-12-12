#!/usr/bin/python3
"""Module to handle minimum operations"""


def is_prime(number):
    """check if a number is a prime number"""
    if number < 2:
        return False
    root = int(number ** (0.5))
    divisor = 2
    while divisor <= root:
        if (number % divisor) == 0:
            return False
        divisor += 1
    return True


def lowest_divisor(number):
    """get lowest divisor of a number"""
    if number < 2:
        return 1
    root = int(number ** (0.5))
    divisor = 2
    while divisor <= root:
        if (number % divisor) == 0:
            return divisor
        divisor += 1
    return number


def minOperations(n):
    """get minimum operations"""
    if n < 2:
        return 0
    totalOperation = 0
    divided = n
    while not is_prime(divided):
        divisor = lowest_divisor(divided)
        divided = int(divided / divisor)
        totalOperation += divisor
    totalOperation += divided
    return totalOperation
