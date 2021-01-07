"""
Given a positive integer n , determine how many different ways it can be
expressed as a sum of consecutive positive integers, and return that count.
"""


def count_consecutive_summers(n):
    count, num = 1, 1
    while num*(num + 1) < 2*n:
        m = (n - (num * (num + 1)) // 2) / (num + 1)
        if (m - int(m) == 0):
            count += 1
        num += 1
    return count
