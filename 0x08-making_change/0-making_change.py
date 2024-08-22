#!/usr/bin/python3
"""Making Change problem"""


def makeChange(coins, total):
    """Computes the minimum number of coins that summed up to
    total
    Arguments:
      - coins: list of integers
      - total: int
    Return
      - minimum number of coins that sums up to total
      - 0 if total is 0
      - -1 if total cannot be met
    """

    if total <= 0:
        return 0

    cache = [total + 1 for x in range(total + 1)]
    cache[0] = 0
    coins = list(sorted(coins))

    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                min_sol = cache[i - coin] + 1
                cache[i] = min(min_sol, cache[i])

    if cache[-1] == total + 1:
        return -1
    return cache[-1]
