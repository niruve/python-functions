"""
Given a string of digits that is guaranteed to contain only digit characters
from '0123456789', read that string "out loud" by saying how many times each
digit occurs consecutively in the current bunch of digits, and then return the
string of digits that you just said out loud.
"""


def count_and_say(digits):
    count = 0
    prev = digits[0]
    result = []
    digits += '%%'
    for i in digits:
        if i == prev:
            count += 1
        else:
            count = str(count)
            result.append(count)
            result.append(prev)
            prev = i
            count = 1
    return ''.join(result)
