"""
Description:
Given a List [] of n integers , find minimum number to be inserted in a list,
so that sum of all elements of list should equal the closest prime number.
"""
prime_divs = [2, 3, 5, 7]


def is_prime(n):
    if n in prime_divs:
        return 1
    for i in prime_divs:
        if n % i == 0:
            return 0
    for i in range(11, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    else:
        prime_divs.append(n)
    return 1


def minimum_number(numbers):
    num = sum(numbers)
    if is_prime(num):
        return 0
    for i in range(1, num):
        if is_prime(num + i):
            return i
    return 0


if __name__ == "__main__":
    print(minimum_number([3, 1, 2]))
