""""
Description:
Given an array/list [] of integers , Find all the LEADERS in the array.

An element is leader if it is greater than The Sum all the elements to its right
side.
"""


def array_leaders(numbers):
    ar_sum = sum(numbers)
    res = list()
    for i in numbers:
        ar_sum -= i
        if i > ar_sum:
            res.append(i)
    return res


if __name__ == "__main__":
    print(array_leaders([16, 17, 4, 3, 5, 2]))
