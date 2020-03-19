"""
Description:
Given an array/list [] of n integers , Separate The even numbers from the odds,
or Separate the men from the boys.
"""


def men_from_boys(arr):
    odd = [i for i in set(arr) if i % 2]
    even = [i for i in set(arr) if i % 2 == 0]
    return sorted(even) + sorted(odd, reverse=True)
