"""
Description:
A format for expressing an ordered list of integers is to use a comma separated
list of either:
    - individual integers
    - or a range of integers denoted by the starting integer separated from the
      end integer in the range by a dash, '-'. The range includes all integers in
      the interval including both endpoints. It is not considered a range unless
      it spans at least 3 numbers. For example ("12, 13, 15-17")

Complete the solution so that it takes a list of integers in increasing order
and returns a correctly formatted string in the range format.
"""


def make_range(args, start_pos, end_pos):
    res = list()
    if end_pos - start_pos < 2:
        for j in range(start_pos, end_pos + 1):
            res.append(str(args[j]))
    else:
        res.append(f"{args[start_pos]}-{args[end_pos]}")
    return res


def solution(args):
    res = list()
    print(args)
    if len(args) <= 2:
        return args
    args.sort()
    start_pos = end_pos = 0
    for i in range(1, len(args)):
        if args[i] - args[i - 1] == 1:
            end_pos += 1
        else:
            res += make_range(args, start_pos, end_pos)
            # if i != len(args) - 1 and end_pos - start_pos >= 2:
            #     res += ','
            start_pos = end_pos = i
        if i == len(args) - 1:
            res += make_range(args, start_pos, end_pos)
    print(res)
    return ','.join(res)


if __name__ == "__main__":
    print(solution(
        [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19,
         20]))
    assert solution(
        [-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19,
         20]) == '-6,-3-1,3-5,7-11,14,15,17-20'
    assert solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]) == \
           '-3--1,2,10,15,16,18-20'
