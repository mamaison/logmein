from deck import Deck
from player import Player
from card import Suits, suit_names, card_names

max_players = 8
max_decks = 4


class Game(object):

    def __init__(self):
        self.cards = []
        self.players = {}
        self.cards.extend(Deck().cards)
        self.decks = 1
        self.available_decks = []

    def add_deck(self):
        if self.decks < 4:
            self.cards.extend(self.available_decks.pop().cards)
            self.decks += 1
            return True
        return False

    def create_deck(self):
        self.available_decks.append(Deck())
        return True

    def add_player(self):
        if len(self.players) == max_players:
            return False
        player = Player(len(self.players) + 1)
        self.players[str(player.get_name())] = player
        return True

    def remove_player(self, guid):
        try:
            del(self.players[guid])
            return True
        except:
            return False

    def get_player(self, guid):
        try:
            self.players[guid]
            return self.players[guid]
        except:
            return None

    def deal_card(self, guid):
        card = self.cards.pop(0)
        result = self.players[guid].add_card(card)
        if result is True:
            return True
        self.cards.insert(0, card)
        return False

    def get_count_by_suits(self):
        hearts = list(filter(lambda x: x.suit == Suits.Hearts, self.cards))
        spades = list(filter(lambda x: x.suit == Suits.Spades, self.cards))
        diamonds = list(filter(lambda x: x.suit == Suits.Diamonds, self.cards))
        clubs = list(filter(lambda x: x.suit == Suits.Clubs, self.cards))
        return {
            suit_names[Suits.Hearts.value]: len(hearts),
            suit_names[Suits.Diamonds.value]: len(diamonds),
            suit_names[Suits.Spades.value]: len(spades),
            suit_names[Suits.Clubs.value]: len(clubs)
        }

    def get_count_by_cards(self):
        cards = {}
        for suit in Suits:
            cards[suit_names[suit.value]] = []
            suit_cards = list(filter(lambda c: c.suit == suit,self.cards))
            sorted_cards = sorted(suit_cards, key=lambda c: c.value, reverse=True)
            for value in range(1,14):
                count = len(list(filter(lambda x: x.value == value, sorted_cards)))
                if count >0:
                    cards[suit_names[suit.value]].append({card_names[value]: count})
        return cards




