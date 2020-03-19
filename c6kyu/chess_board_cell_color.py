"""
Description:

Given two cells on the standard chess board, determine whether they have the
same color or not.
"""


def chess_board_cell_color(cell1, cell2):
    cell1_xy = (ord(cell1[0].lower()) - ord('a') + 1, int(cell1[1]))
    cell2_xy = (ord(cell2[0].lower()) - ord('a') + 1, int(cell2[1]))
    return sum(cell1_xy) % 2 == sum(cell2_xy) % 2


if __name__ == "__main__":
    print(chess_board_cell_color('A1', 'C4'))