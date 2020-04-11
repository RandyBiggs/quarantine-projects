class Hand:
    # Default constructor
    def __init__(self):
        self.cards = []
        self.max_size = 5

    def draw_card(self, card):
        if len(self.cards) < self.max_size:
            self.cards.append(card)

    def __repr__(self):
        ret_str = ''
        for card in self.cards:
            ret_str += str(card) + "\n"
        return ret_str
