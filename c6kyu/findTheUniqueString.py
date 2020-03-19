"""
Description:
There is an array of strings. All strings contains similar letters except one.
Try to find it!

url: https://www.codewars.com/kata/585d8c8a28bc7403ea0000c3
"""


def find_uniq(arr):
    index = 0
    res = [set(x.replace(' ', '').lower()) if isinstance(x, str) else x for x in arr]
    for i in range(len(arr)):
        if res[i] != res[i - 1] and res[i] != res[(i + 1) % len(res)]:
            index = i
    return arr[index]


if __name__ == "__main__":
    print(find_uniq(['Aa', 'aaa', 'aaaaa', 4, 'Aaaa', 'AaAaAa', 'a']),
          'BbBb')
