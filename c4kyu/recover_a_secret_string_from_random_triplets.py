""""
Description:

There is a secret string which is unknown to you. Given a collection of random
triplets from the string, recover the original string.

A triplet here is defined as a sequence of three letters such that each letter
occurs somewhere before the next in the given string. "whi" is a triplet for the
 string "whatisup".

As a simplification, you may assume that no letter occurs more than once in the
secret string.
"""
from itertools import chain


def recoverSecret(triplets):
    unique_letters = set(chain.from_iterable(triplets))
    dict_ = dict(
        zip(unique_letters, [set() for _ in range(len(unique_letters))]))
    for triplet in triplets:
        for i, letter in enumerate(dict_.keys()):
            if triplet[0] == letter:
                dict_[letter].add(triplet[1])
                dict_[letter].add(triplet[2])
            elif triplet[1] == letter:
                dict_[letter].add(triplet[2])
    for letter in dict_.keys():
        temp_set = set()
        for second_letter in dict_[letter]:
            temp_set |= dict_[second_letter]
        dict_[letter] |= temp_set
    # print(sorted(dict_, key=lambda x: len(dict_[x]), reverse=True))
    return "".join(sorted(dict_, key=lambda x: len(dict_[x]), reverse=True))


if __name__ == "__main__":
    secret = "whatisup"
    triplets = [
        ['t', 'u', 'p'],
        ['w', 'h', 'i'],
        ['t', 's', 'u'],
        ['a', 't', 's'],
        ['h', 'a', 'p'],
        ['t', 'i', 's'],
        ['w', 'h', 's']
    ]

    print(recoverSecret(triplets))
