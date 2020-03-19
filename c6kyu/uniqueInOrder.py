"""
Description:
Implement the function unique_in_order which takes as argument a sequence and
returns a list of items without any elements with the same value next to each
other and preserving the original order of elements.

url: https://www.codewars.com/kata/54e6533c92449cc251001667
"""


def unique_in_order(iterable):
    res = list()
    if iterable:
        res.append(iterable[0])
        [res.append(x) for x in iterable if x != res[-1]]
    return res
