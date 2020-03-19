from collections import Counter


def anagrams(word, words):
    source_word = Counter(word)
    res = list()
    for contender in words:
        if Counter(contender) == source_word:
            res.append(contender)
    return res


if __name__ == "__main__":
    assert anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa']
    assert anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == ['carer', 'racer']