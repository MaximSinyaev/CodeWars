"""
Description:

Complete the function that determines the score of a hand in the card game
Blackjack (aka 21).

The function receives an array of strings that represent each card in the hand
("2", "3", ..., "10", "J", "Q", "K" or "A") and should return the score of the
hand (integer).
"""
card_with_pictures = 'JQK'


def score_hand(cards):
    sum_num_cards = sum([int(i) for i in cards if i.isdigit()])
    sum_pict_carts = sum([10 for i in cards if i in card_with_pictures])
    total_score = sum_num_cards + sum_pict_carts
    if 'A' in cards:
        for _ in range(cards.count('A')):
            if 21 - total_score - (cards.count('A') - 1) >= 11:
                total_score += 11
            else:
                total_score += 1
    return total_score


if __name__ == "__main__":
    print(score_hand(['A', 'A', 'A', 'J']))
