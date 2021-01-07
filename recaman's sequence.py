
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
