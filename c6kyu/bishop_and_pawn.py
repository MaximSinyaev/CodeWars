"""
Description:

Given the positions of a white bishop and a black pawn on the standard chess
board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to
diagonal movement.
"""


def bishop_and_pawn(bishop, pawn):
    bishop_coords = (ord(bishop[0].lower()) - ord('a') + 1, int(bishop[1]))
    pawn_coords = (ord(pawn[0].lower()) - ord('a') + 1, int(pawn[1]))
    # if pawn is on the same diagonal then difference between their coordinates
    # will be the same |x1 - x2| == |y1 - y2|
    return abs(bishop_coords[0] - pawn_coords[0]) == \
            abs(bishop_coords[1] - pawn_coords[1])

if __name__ == "__main__":
    tests = [
        # [[bishop, pawn], expected]
        [["a1", "c3"], True],
        [["h1", "h3"], False],
        [["a5", "c3"], True],
        [["g1", "f3"], False],
    ]

    for coords, res in tests:
        assert bishop_and_pawn(*coords) == res