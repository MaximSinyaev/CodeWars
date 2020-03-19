from collections import Counter


def duplicate_count(text):
    counter = Counter(text.lower())
    k = 0
    for i in counter.values():
        if i > 1:
            k += 1
    return k