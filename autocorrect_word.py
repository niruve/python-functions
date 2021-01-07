"""
Given a word, a list of words, and a distance function df that tells how "far"
the first argument is from the second (for example, df('a','s') == 1 and
df('a', 'a') == 0 ), this functions will find and return the word in the list
of words that have the same number of letters and whose distance, measured as
the sum of the distances of the characters in the same position, is the
smallest. If there exist several words equidistant from word, return the first
such word in the dictionary order.
"""


def autocorrect_word(word, words, df):
    best, lowest = '', 100
    words = [w for w in words if len(w) == len(word)]
    for w in words:
        dist = sum((df(x, y) for (x, y) in zip(w, word)))
        if dist < lowest:
            lowest = dist
            best = w
    return best
