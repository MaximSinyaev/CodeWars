"""
Description:
Given an array of integers , Find the maximum product obtained from multiplying
2 adjacent numbers in the array.
"""


def adjacent_element_product(array):
    max_prod = array[0] * array[1]
    for pair in zip(array[:-1], array[1:]):
        if pair[0] * pair[1] > max_prod:
            max_prod = pair[0] * pair[1]
    return max_prod

