"""
Description:
Given a positive integral number n, return a strictly increasing sequence
(list/array/string depending on the language) of numbers, so that the sum of the
 squares is equal to n².

If there are multiple solutions (and there will be), return as far as possible
the result with the largest possible values:
"""


def recursion_decompose(n, seq, square):
    # if n == 1:
    #     seq.append(1)
    #     return seq
    print("recursion:", seq, n, square)
    temp_sum = sum([x ** 2 for x in seq]) if seq else 0
    if temp_sum == square:
        print("It's here")
        return seq
    # if sum(range(n)) + sum(seq) < n ** 0.5:
    #     return list()
    if n == 0:
        seq.pop()
        return seq
    # if sum([x ** 2 for x in seq]) > square:
    #     print("Too much")
    #     seq.pop()
    #     return seq
    if n ** 2 == square:
        n -= 1
    for i in range(n, 0, -1):
        if temp_sum + i ** 2 <= square:
            seq.append(i)
            seq = recursion_decompose(i - 1, seq, square)
        if seq and sum([x ** 2 for x in seq]) == square:
            print("I found")
            return seq
        # elif not seq:
        #     return None
    return seq


def decompose(n):
    seq = recursion_decompose(n, list(), int(n ** 2))
    return sorted(seq) if seq else None
    threshold = int(n ** 2)
    squares = [i ** 2 for i in range(n - 1, 0, -1)]



if __name__ == "__main__":
    print("> Result:", decompose(50))
    print("> Result:", decompose(100))
    print("> Result:", decompose(50))
