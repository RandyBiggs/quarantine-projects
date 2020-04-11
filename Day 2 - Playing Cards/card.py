from random import randint


class Card:
    # Default constructor
    def __init__(self, suit, value):

        self.suits = {
            1: 'Hearts',
            2: 'Diamonds',
            3: 'Spades',
            4: 'Clubs'
        }
        self.values = {
            1: 'Ace',
            2: '2',
            3: '3',
            4: '4',
            5: '5',
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: '10',
            11: 'Jack',
            12: 'Queen',
            13: 'King'
        }
        self.card = self.values[value] + " of " + self.suits[suit]

    # Print the card
    def __repr__(self):
        return self.card
