from card import Suits, Card
from utils import shuffle_cards


class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in Suits:
            for i in range(1, 14):
                self.cards.append(Card(i, suit))
        shuffle_cards(self.cards)
