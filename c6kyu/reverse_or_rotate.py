"""
Description:

The input is a string str of digits. Cut the string into chunks (a chunk here is
a substring of the initial string) of size sz (ignore the last chunk if its
size is less than sz).

If a chunk represents an integer such as the sum of the cubes of its digits is
divisible by 2, reverse that chunk; otherwise rotate it to the left by one
position. Put together these modified chunks and return the result as a string.
"""


def check_number(str_num):
    return not sum(map(int, list(str_num))) % 2


def str_reverse(string):
    return "".join([symb for symb in string[::-1]])


def revrot(strng, sz):
    res = ""
    if sz <= 0 or not strng:
        return res
    for i in range(len(strng) // sz):
        # print(strng[i * sz:(i + 1) * sz])
        if len(strng[i * sz:]) < sz:
            return res
        if check_number(strng[i * sz:(i + 1) * sz]):
            # print(str_reverse(strng[i * sz:(i + 1) * sz]))
            res += str_reverse(strng[i * sz:(i + 1) * sz])
        else:
            res += strng[i * sz + 1:(i + 1) * sz] + strng[i * sz]
    return res


if __name__ == "__main__":
    s = "73304991087281576455176044327690580265896"
    ans = "1994033775182780067155464327690480265895"
    print(revrot(s, 8), ans, sep="\n")
    assert revrot(s, 8) == ans
