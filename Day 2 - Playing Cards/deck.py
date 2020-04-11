from random import randint
import card as c


class Deck:
    # Default constructor
    def __init__(self):
        self.deck = []
        for i in range(4):
            suit = i+1
            for j in range(13):
                value = j+1
                card = c.Card(suit, value)
                self.deck.append(card)

    # Print each card currently in the deck
    def __repr__(self):
        ret_str = ''
        for card in self.deck:
            ret_str += repr(card) + '\n'
        return ret_str

    def draw_card(self):
        card = None
        rng = randint(0, 51)
        try:
            card = self.deck[rng]
        except KeyError:
            print("Deck is Empty")
        return card

    def shuffle_deck(self):
        shuffled_deck = []
        while self.deck:
            deck_size = len(self.deck)
            rng = randint(0, deck_size-1)
            shuffled_deck.append(self.deck.pop(rng))
            deck_size -= 1
        self.deck = shuffled_deck
        return self.deck


