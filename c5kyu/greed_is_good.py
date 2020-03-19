"""
Description:

Greed is a dice game played with five six-sided dice. Your mission, should you
choose to accept it, is to score a throw according to these rules. You will
always be given an array with five six-sided dice values.

    Three 1's => 1000 points
    Three 6's =>  600 points
    Three 5's =>  500 points
    Three 4's =>  400 points
    Three 3's =>  300 points
    Three 2's =>  200 points
    One   1   =>  100 points
    One   5   =>   50 point
"""


def score(dice):
    total_scores = 0
    ones = dice.count(1)
    fives = dice.count(5)
    if ones >= 3:
        total_scores += 1000
    total_scores += ones % 3 * 100 + fives % 3 * 50
    for i in range(2, 7):
        if dice.count(i) > 2:
            total_scores += i * 100
    return total_scores
