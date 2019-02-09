from uuid import uuid4
from functools import reduce

sequence_to_letter = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}

class Player(object):

    def __init__(self, sequence):
        self.cards =[]
        self.sequence = sequence
        self.guid = uuid4()

    def add_card(self, card):
        self.cards.append(card)
        return True

    # Cette methode n'est pas utile en Python. Je la mets ici simplement a titre indicatif
    def get_cards(self):
        return list(map(lambda c: c.get_name(),self.cards))

    def get_name(self):
        return str("Player-" + sequence_to_letter[self.sequence])

    def get_total(self):
        if len(self.cards) > 0:
            total = 0
            for card in self.cards:
                total += card.value
            return total
        return 0

    def to_dict(self):
        return {
            'name': self.get_name(),
            'cards': list(map(lambda c: c.get_name(),self.cards)),
            'total': self.get_total()
        }
