"""
Description:
The new "Avengers" movie has just been released! There are a lot of people at
the cinema box office standing in a huge line. Each of them has a single 100,
50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

url: https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8
"""

from collections import defaultdict


def tickets(people):
    money = defaultdict(int)
    for bill in people:
        if bill == 50:
            if money[25]:
                money[25] -= 1
            else:
                return "NO"
            money[50] += 1
        elif bill == 100:
            if money[25] and money[50]:
                money[25] -= 1
                money[50] -= 1
            elif money[25] >= 3:
                money[25] -= 3
            else:
                return "NO"
            money[100] += 1
        else:
            money[25] += 1
    return "YES"


if __name__ == "__main__":
    print(tickets([25, 25, 50]), "YES")
    print(tickets([25, 25, 25, 100]), "YES")