"""
Description:

You are now to create a function that returns a Josephus permutation, taking as
parameters the initial array/list of items to be permuted as if they were in a
circle and counted out every k places until none remained.
"""


def josephus(items, k):
    length = len(items)
    res = list()
    k -= 1
    pos = 0
    while items:
        if pos + k >= length:
            pos = (k + pos) % length
            res.append(items.pop(pos))
        else:
            pos += k
            res.append(items.pop(pos))
        length = len(items)
    return res


if __name__ == "__main__":
    print(josephus([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
