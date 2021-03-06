"""
This function represents Zeckendorf's theorem that every positive integer n can
be expressed as the sum of one or more distinct non-consecutive Fibonacci
numbers. For clarity, the list is sorted in descending order.
"""


def fibonacci_sum(n):
    from bisect import bisect_left
    seq = [1, 2, 3, 5, 8, 13, 21]
    result = []
    while n > seq[-1]:
        seq.append(seq[-1] + seq[-2])
    j = bisect_left(seq, n)
    while n > 0:
        if n >= seq[j]:
            result.append(seq[j])
            n -= seq[j]
            j -= 2
        else:
            j -= 1
    return result
