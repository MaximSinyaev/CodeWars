"""
Description:
Divisors of 42 are : 1, 2, 3, 6, 7, 14, 21, 42. These divisors squared are: 1,
4, 9, 36, 49, 196, 441, 1764. The sum of the squared divisors is 2500 which is
50 * 50, a square!

Given two integers m, n (1 <= m <= n) we want to find all integers between m and
 n whose sum of squared divisors is itself a square. 42 is such a number.

The result will be an array of arrays or of tuples (in C an array of Pair) or a
string, each subarray having two elements, first the number whose squared
divisors is a square and then the sum of the squared divisors.
"""
import math
from itertools import chain
prime_divisors = [1, 2, 3]


def find_divisors(n):
    div = [[i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0]
    return set(chain.from_iterable(div))

def square_factors(n):
    s = sum([i ** 2 for i in find_divisors(n)])
    return s

def list_squared(m, n):
    # find_primes(n)
    res = list()
    for i in range(m, n + 1):
        # seq = find_divisors(i)
        seq = square_factors(i)
        # temp_sum = sum(seq)
        if math.sqrt(seq) % 1 == 0:
            print(seq)
            res.append([i, seq])
    return res


if __name__ == "__main__":
    print(list_squared(1, 500))
    # print(prime_divisors)
