"""
Description:
Your task is to make a simple class called SnakesLadders.
The test cases will call the method play(die1, die2) independantly of the
state of the game or the player turn. The variables die1 and die2 are the
die thrown in a turn and are both integers between 1 and 6. The player will
move the sum of die1 and die2.

"""

from collections import defaultdict

snakes = {
    16: 6,
    46: 25,
    49: 11,
    62: 19,
    64: 60,
    74: 53,
    89: 68,
    92: 88,
    95: 75,
    99: 80
}

stairs = {
    2: 38,
    7: 14,
    8: 31,
    15: 26,
    21: 42,
    36: 44,
    28: 84,
    51: 67,
    71: 91,
    78: 98,
    87: 94
}


class SnakesLadders():

    def __init__(self, n_players=2):
        self.n_players = n_players
        self.players = defaultdict()
        for i in range(1, n_players + 1):
            self.players[i] = [0, 0]
        self.map = self.init_map()
        self.end = 0
        self.move = 0

    def play(self, die1, die2):
        if self.end:
            return 'Game over!'
        for i, player in self.players.items():
            if player[1] == self.move:
                self.players[i][0] += die1 + die2
                if self.players[i][0] > 100:
                    self.players[i][0] -= 2 * self.players[i][0] % 100
                elif self.players[i][0] == 100:
                    self.end = 1
                    return f'Player {i} Wins!'
                if self.map[self.players[i][0] // 10][self.players[i][0] % 10 ]:
                    self.players[i][0] = self.map[self.players[i][0] // 10] \
                        [self.players[i][0] % 10]
                self.players[i][1] += 1 if die2 != die1 else 0
                return f'Player {i} is on square {self.players[i][0]}'
            if i == self.n_players:
                self.move += 1
                return self.play(die1, die2)

    def init_map(self):
        map = [[0 for _ in range(10)]
               for i in range(10)]
        for coord in snakes.items():
            map[coord[0] // 10][coord[0] % 10] = coord[1]
        for coord in stairs.items():
            map[coord[0] // 10][coord[0] % 10] = coord[1]
        return map


if __name__ == "__main__":
    game = SnakesLadders()
    for i in range(100):
        print(game.play(1, 3))
    # print(game.play(1, 1))
    # print(game.play(1, 5))
    # print(game.play(6, 2))
    # print(game.play(1, 1))
    # print(game.play(1, 1))
