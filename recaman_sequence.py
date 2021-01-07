"""
This function computes and returns the first n terms of the Recaman's sequence,
where the first term a_1 = 1. To increase efficiency, a set is used to keep
track of which values have already been part of the previously generated
sequence in order to generate each element in constant time.
"""


def recaman(n):
    seq = set()
    result = [0]*(n+1)

    for i in range(1, n+1):
        if result[i-1] - i not in seq and result[i-1] - i > 0:
            result[i] = result[i-1] - i
            seq.add(result[i])
        else:
            result[i] = result[i-1] + i
            seq.add(result[i])
    return result[1:]
