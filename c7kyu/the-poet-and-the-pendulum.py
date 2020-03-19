"""
Description:
Given an array/list [] of n integers , Arrange them in a way similar to the to-and-fro movement of a Pendulum

    - The Smallest element of the list of integers , must come in center
      position of array/list.
        - The Higher than smallest , goes to the right .

    - The Next higher number goes to the left of minimum number and So on,
      in a to-and-fro manner similar to that of a Pendulum.

"""


def pendulum(values):
    values.sort()
    res = [0 for _ in range(len(values))]
    begin = len(values) // 2
    if len(values) % 2:
        begin = len(values) // 2
        res[begin] = values[0]
        for i in range(1, len(values)):
            if i % 2:
                res[begin + (i + 1) // 2] = values[i]
            else:
                res[begin - (i + 1) // 2] = values[i]
    else:
        begin = (len(values) - 1) // 2
        for i in range(len(values)):
            if i % 2:
                res[begin + (i + 1) // 2] = values[i]
            else:
                res[begin - (i + 1) // 2] = values[i]
    return res

if __name__ == "__main__":
    print(pendulum([4,6,7,5]))