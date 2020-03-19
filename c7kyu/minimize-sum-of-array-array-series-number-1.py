"""
Description:

Given an array of integers , Find the minimum sum which is obtained from summing
each Two integers product .
"""
def min_sum(arr):
    arr.sort()
    end = len(arr)
    sum = 0
    # print(arr[:end // 2], arr[-1:end // 2 - 1:-1])
    for pair in zip(arr[:end // 2], arr[-1:end // 2 - 1:-1]):
        sum += pair[0] * pair[1]
    return sum


if __name__ == "__main__":
    min_sum(list(range(10)))
