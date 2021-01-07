"""
This function will determine whether the positive integer n is a cyclops
number. A nonnegative integer is said to be a cyclops number if it consists of
an odd number of digits so that the middle digit is a zero and all other digits
of that number are nonzero.
"""


def is_cyclops(n):
    s = str(n)
    seq = list(s)
    mid = len(s)//2
    if len(s) % 2 != 0 and seq[mid] == '0' and seq.count('0') == 1:
        return True
    else:
        return False
