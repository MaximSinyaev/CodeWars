"""
Description:
Your goal in this kata is to implement a difference function, which subtracts
one list from another and returns the result.

url: https://www.codewars.com/kata/523f5d21c841566fde000009
"""


def array_diff(a, b):
    return [x for x in a if x not in b]
