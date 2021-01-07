"""
When given a list of items whose length is guaranteed to be even, this function
will create and return a list made by performing a perfect riffle to the items.
Also known as the Faro Shuffle, the list of items is divided into two equal
sized halves and then are interweaved in an alternative fashion. The parameter
out determines whether the function performs an out shuffle or an in shuffle,
which determines which half is taken first.

"""


def riffle(items, out):
    list1 = items[:(len(items)//2)]
    list2 = items[(len(items)//2):]
    words = []

    if items == []:
        return True
    elif out is True:
        for i in range(len(items)//2):
            words.append(list1[i])
            words.append(list2[i])
        return words
    else:
        for i in range(len(items)//2):
            words.append(list2[i])
            words.append(list1[i])
    return words
