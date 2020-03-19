"""
Description:
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

url: https://www.codewars.com/kata/576757b1df89ecf5bd00073b
"""

def tower_builder(n_floors):
    res = [str() for _ in range(n_floors)]
    for i in range(n_floors):
        side = ' ' * (n_floors - 1)
        center = '*' * (i + 1)
        res[i] += side + center
    return res