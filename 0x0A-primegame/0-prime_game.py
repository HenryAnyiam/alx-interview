#!/usr/bin/python3
"""module to handle a prime game"""


def switch_player(player: str) -> str:
    """switch player turn"""
    if player == "Maria":
        return "Ben"
    return "Maria"


def get_primes(num: int) -> int:
    """get prime numbers in the number range"""
    primes = [1]
    prime = True
    if num < 2:
        return primes
    for i in range(2, num):
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime:
            primes.append(i)
    return primes


def play(num: int) -> str:
    """play game"""
    if num <= 1:
        return "Ben"
    player = "Maria"
    num_range = [i for i in range(1, num)]
    primes = get_primes(num)
    while primes:
        pick = primes.pop(0)
        temp = num_range.copy()
        for i in temp:
            if i % pick == 0:
                num_range.remove(i)
        player = switch_player(player)
    return player


def isWinner(x: int, nums: list) -> str:
    """find winner of prime game"""
    players = {"Maria": 0, "Ben": 0}
    if not isinstance(x, int) or not isinstance(nums, list):
        return None
    if x > len(nums):
        return None
    for i in range(x):
        if not isinstance(nums[i], int):
            return None
        win = play(nums[i])
        players[win] += 1
    if players["Maria"] > players["Ben"]:
        return "Maria"
    return "Ben"
