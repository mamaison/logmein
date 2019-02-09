from enum import Enum


class Suits(Enum):
    Hearts = 1
    Spades = 2
    Clubs = 3
    Diamonds = 4


suit_names = {1: 'Hearts', 2: 'Spades', 3: 'Clubs', 4: 'Diamonds'}
card_names = {1: 'Ace', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'jack', 12: 'queen', 13: 'king'}


class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    # Cette methode n'est pas utile en Python. Je la mets ici simplement a titre indicatif
    def get_value(self):
        return self.value;

    def get_name(self):
        return f'{card_names[self.value]} of {suit_names[self.suit.value]}'
