"""
Description:
Given a sequence of n integers , separate the negative numbers (chaff) from
positive ones (wheat).
"""


def wheat_from_chaff(values):
    last_index = len(values) - 1
    for i in range(len(values)):
        if values[i] > 0:
            for j in range(last_index, i, -1):
                if values[j] < 0:
                    last_index = j
                    values[i], values[j] = values[j], values[i]
                    break
    return values

if __name__ == "__main__":
    print(wheat_from_chaff([2, -4, 6, -6]))
