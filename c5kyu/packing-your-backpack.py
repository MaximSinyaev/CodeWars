"""
Description:
Your input will consist of two arrays, one for the scores and one for the
weights. You input will always be valid lists of equal length, so you don't have
to worry about verifying your input.

You'll also be given a maximum weight. This is the weight that your backpack
cannot exceed.
"""

def pack_bagpack(scores, weights, capacity):
    values = dict(zip(range(len(weights)), [score / weight for weight, score in
                                            zip(weights, scores)]))
    values = sorted(values.items(), key=lambda x: x[1], reverse=True)
    sum = 0
    i = 0
    print(values)
    while capacity and i < len(values):
        if weights[values[i][0]] <= capacity:
            sum += values[i][1] * weights[values[i][0]]
            capacity -= weights[values[i][0]]
        i += 1
    return int(sum)

if __name__ == "__main__":
    print(pack_bagpack([15, 10, 9, 5], [1, 5, 3, 4], 8))
    print(pack_bagpack([20, 5, 10, 40, 15, 25], [1, 2, 3, 8, 7, 4], 10))
