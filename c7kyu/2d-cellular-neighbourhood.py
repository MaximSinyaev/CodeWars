""""
Description:

The neighbourhood of a cell (in a matrix) are cells that are near to it. There
are two popular types:

    - The Moore neighborhood are eight cells which surround a given cell.
    - The Von Neumann neighborhood are four cells which share a border with the
      given cell.

Given a neighbourhood type ("moore" or "von_neumann"), a 2D matrix (a list of
lists) and a pair of coordinates, return the list of neighbours of the
given cell.
"""


def get_neighbourhood(n_type, mat, coordinates):
    res = []
    # Explore width and height
    h = len(mat)
    w = len(mat[0])
    # Check if coords suits matrices
    if coordinates[0] >= h or coordinates[1] >= w or not mat:
        return res
    # Search for Von Neumann neighborhood cells
    if coordinates[0] - 1 >= 0:
        res.append(mat[coordinates[0] - 1][coordinates[1]])
    if coordinates[1] - 1 >= 0:
        res.append(mat[coordinates[0]][coordinates[1] - 1])
    if coordinates[0] + 1 < h:
        res.append(mat[coordinates[0] + 1][coordinates[1]])
    if coordinates[1] + 1 < w:
        res.append(mat[coordinates[0]][coordinates[1] + 1])
    # Return Von Neumann's coords if needed
    if n_type == 'von_neumann':
        return res
    if coordinates[0] - 1 >= 0 and coordinates[1] - 1 >= 0:
        res.append(mat[coordinates[0] - 1][coordinates[1] - 1])
    if coordinates[0] + 1 < h and coordinates[1] - 1 >= 0:
        res.append(mat[coordinates[0] + 1][coordinates[1] - 1])
    if coordinates[0] - 1 >= 0 and coordinates[1] + 1 < w:
        res.append(mat[coordinates[0] - 1][coordinates[1] + 1])
    if coordinates[0] + 1 < h and coordinates[1] + 1 < w:
        res.append(mat[coordinates[0] + 1][coordinates[1] + 1])
    return res


if __name__ == "__main__":
    N = 5
    M = 5
    mat = [[j + i * N for j in range(N)] for i in range(M)]

    indexes1 = (1, 1)
    expected_moore_1 = [1, 0, 2, 5, 7, 10, 11, 12]
    expected_von_neumann_1 = [1, 5, 7, 11]
    print(sorted(get_neighbourhood('moore', mat, indexes1)),
          sorted(expected_moore_1))
    print(sorted(get_neighbourhood('von_neumann', mat, indexes1)),
          sorted(expected_von_neumann_1))

    indexes2 = (0, 0)
    expected_moore_2 = [1, 6, 5]
    expected_von_neumann_2 = [1, 5]
    print(sorted(get_neighbourhood('moore', mat, indexes2)),
          sorted(expected_moore_2))
    print(sorted(get_neighbourhood('von_neumann', mat, indexes2)),
          sorted(expected_von_neumann_2))
