"""
Description:
You will be given a 2D array of the maze
and an array of directions. Your task is to follow
the directions given. If you reach the end point before all your moves have
gone, you should return Finish. If you hit any walls or go outside the maze
border, you should return Dead. If you find yourself still in the maze after
using all the moves, you should return Lost.

"""


def maze_runner(maze, directions):
    n = len(maze)
    dirs_dict = {
        'N': -n,
        'S': n,
        'E': 1,
        'W': -1
    }
    flat_map = list()
    [flat_map.extend(row) for row in maze]
    position = flat_map.index(2)
    for move in directions:

        temp = position % n
        print(temp, position, flat_map[position], move)
        position += dirs_dict[move]
        # print(, temp, dirs_dict[move] % n)
        if (position // n not in range(n)) \
                or (
                (temp + dirs_dict[move] if move in 'WE' else 0) not in range(n)) \
                or flat_map[position] == 1:
            return 'Dead'
        if flat_map[position] == 3:
            return 'Finish'
    return 'Lost'


maze = [[1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 3],
        [1, 0, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [1, 2, 1, 0, 1, 0, 1]]

maze = [[1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 3, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 1, 2, 1]]

if __name__ == '__main__':
    print(maze_runner(maze,
                      ["N", "N", "N", "W", "E", "W", "S", "S", "S",
                       "S", "S"]))
