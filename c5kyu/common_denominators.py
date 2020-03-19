"""
Description:

You will have a list of rationals in the form:
    { {numer_1, denom_1} , ... {numer_n, denom_n} },
                                where all numbers are positive ints.

You have to produce a result in the form:
    (N_1, D) ... (N_n, D)
"""


def gcd(a, b):
    if a < b:
        a, b = b, a
    if b <= 1:
        return 1
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def reduce_fraction(numerator, denominator):
    common_div = gcd(numerator, denominator)
    if common_div != 1:
        numerator //= common_div
        denominator //= common_div
    return [numerator, denominator]


def convertFracts(lst):
    common_denom = 1
    for i in range(len(lst)):
        lst[i] = reduce_fraction(*lst[i])
    for i in range(len(lst)):
        fraction = lst[i]
        common_div = gcd(fraction[1], common_denom)
        print(fraction, common_div, common_denom)
        prev_denom = fraction[1]
        fraction[0] *= common_denom // common_div
        fraction[1] *= common_denom // common_div
        common_denom *= prev_denom // common_div
    for i in range(len(lst) - 1, -1, -1):
        fraction = lst[i]
        common_div = gcd(fraction[1], common_denom)
        print(fraction, common_div, common_denom)
        prev_denom = fraction[1]
        fraction[0] *= common_denom // common_div
        fraction[1] *= common_denom // common_div
        common_denom *= prev_denom // common_div
    return lst


if __name__ == "__main__":
    a = [[1, 2], [1, 3], [1, 4]]
    b = [[6, 12], [4, 12], [3, 12]]
    print(convertFracts(a))