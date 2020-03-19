"""
Description:

Basically you have to assume that n people are put into a circle and that they
are eliminated in steps of k elements, like this:

josephus_survivor(7,3) => means 7 people in a circle;
one every 3 is eliminated until one remains
[1,2,3,4,5,6,7] - initial sequence
[1,2,4,5,6,7] => 3 is counted out
[1,2,4,5,7] => 6 is counted out
[1,4,5,7] => 2 is counted out
[1,4,5] => 7 is counted out
[1,4] => 5 is counted out
[4] => 1 counted out, 4 is the last element - the survivor!
"""


def josephus_survivor(n, k):
    items = list(range(1, n + 1))
    k -= 1
    pos = 0
    while len(items) != 1:
        pos = (k + pos) % len(items)
        items.pop(pos)
    return items[0]


if __name__ == "__main__":
    print(josephus_survivor(7, 3))