import random

RANKS_VALUES = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 'J': 10, 'Q': 10, 'K': 10}


class Deck:
    def __init__(self):
        self.cards = [2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A'] * 4

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []

    def get_value(self):
        value = 0
        ace_count = 0

        for card in self.cards:
            if card in RANKS_VALUES:
                value += RANKS_VALUES[card]
            else:
                ace_count += 1

        if ace_count > 0:
            if ace_count == 1:
                if value <= 10:
                    value += 11
                else:
                    value += 1

            if ace_count == 2:
                if value <= 9:
                    value += 12
                else:
                    value += 2

            if ace_count == 3:
                if value <= 8:
                    value += 13
                else:
                    value += 3

        return value


class Player:
    def __init__(self):
        self.hand = Hand()
        self.stay = False
        self.bust = False
        self.blackjack = False
