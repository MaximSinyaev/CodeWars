"""
Description:

Given an n x n array, return the array elements arranged from outermost elements
to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
"""

def snail(snail_map):
    n = len(snail_map)
    if n == 0:
        return []
    res = snail_map[0].copy()
    col = n - 1
    row = 0
    step = n - 1
    sign = 1
    while step:
        for i in range(step):
            row += 1 * sign
            res.append(snail_map[row][col])

        for i in range(step):
            col -= 1 * sign
            res.append(snail_map[row][col])

        print(row, col)
        sign *= -1
        step -= 1
    return res


if __name__ == "__main__":
    array = [[1, 2, 3],
             [8, 9, 4],
             [7, 6, 5]]
    expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]
    print(snail(array))