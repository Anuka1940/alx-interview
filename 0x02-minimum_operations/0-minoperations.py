#!/usr/bin/python3
""" A function that returns the minimum operations task"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """
    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    ops, first = 0, 2
    while first <= n:
        # if n evenly divides by first
        if n % first == 0:
            # total even-divisions by first = total operations
            ops += first
            # set n to the remainder
            n = n / first
            # reduce first to find remaining smaller vals that evenly-divide n
            first -= 1
        # increment first until it evenly-divides n
        first += 1
    return ops
