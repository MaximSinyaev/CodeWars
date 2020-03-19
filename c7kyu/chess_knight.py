"""
Description:

Given a position of a knight on the standard chessboard, find the number of
different moves the knight can perform.

"""


def chess_knight(cell):
    cell_xy = (ord(cell[0].lower()) - ord('a') + 1, int(cell[1]))
    res = 0
    desk_range = range(1, 9)
    for y in [-2, -1, 1, 2]:
        for x in [-2, -1, 1, 2]:
            if (x + y) % 2:
                if cell_xy[0] + y in desk_range and cell_xy[1] + x in desk_range:
                    res += 1
    return res


if __name__ == "__main__":
    print(chess_knight("a1"))