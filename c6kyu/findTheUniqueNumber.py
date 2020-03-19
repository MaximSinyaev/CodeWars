"""
Description:
There is an array with some numbers. All numbers are equal except for one.
Try to find it!

url: https://www.codewars.com/kata/585d7d5adb20cf33cb000235
"""
from collections import Counter


def find_uniq(arr):
    count = Counter(arr)
    return count.most_common()[-1][0]

