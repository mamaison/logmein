from flask import Flask
import json
from game import Game
import pickle
import os
from utils import shuffle_cards


app = Flask(__name__)


def save_game(game):
    with open('current_game.p', 'wb') as current_game:
        pickle.dump(game, current_game)


def load_game(func, guid=None):
    try:
        with open('current_game.p', 'rb') as current_game:
            try:
                game = pickle.load(current_game)
                if guid:
                    message = func(game, guid)
                else:
                    message = func(game)
                save_game(game)
                return json.dumps(message)
            except EOFError:
                return json.dumps({'message': 'You must create a game first'})
    except FileNotFoundError:
        return json.dumps({'message': 'You must create a game first'})


@app.route('/game', methods=['POST'])
def create_game():
    game = Game()
    save_game(game)
    return json.dumps({'message': ' New game created'})


@app.route('/game', methods=['DELETE'])
def delete_game():
    try:
        os.remove('current_game.p')
        return json.dumps({'message': 'Game deleted'})
    except FileNotFoundError:
        return json.dumps({'message': 'No game found'})


@app.route('/game/deck', methods=['POST'])
def create_deck():
    def game_create_deck(game):
        if game.create_deck():
            return {'message': 'Deck created'}
    return load_game(game_create_deck)


@app.route('/game/decks', methods=['POST'])
def add_deck():
    def game_add_deck(game):
        if len(game.available_decks) == 0:
            return {'message': 'You must create a deck first'}
        if game.add_deck():
            return {'message': 'Deck added'}
        return {'message': 'Maximum number of decks per game reached'}
    return load_game(game_add_deck)


@app.route('/game/players', methods=['POST'])
def add_player():
    def game_add_player(game):
        if game.add_player():
            return {'message': 'Player added'}
        return {'message': 'Maximum number of players per game reached'}
    return load_game(game_add_player)


@app.route('/game/players/<guid>', methods=['DELETE'])
def remove_player(guid):
    def game_remove_player(game, guid):
        if game.remove_player(guid):
            return {'message': 'Player removed'}
        return {'message': 'Player not founc'}
    return load_game(game_remove_player, guid)


@app.route('/game/players/<guid>/deal-card', methods=['PUT'])
def deal_card(guid):
    def game_deal_card(game, guid):
        player = game.get_player(guid)
        if player:
            if game.deal_card(guid):
                return {'message': 'Card delt'}
        return {'message': 'Player not found'}
    return load_game(game_deal_card, guid)


@app.route('/game/players/<guid>/get-cards', methods=['GET'])
def get_cards_fomr_player(guid):
    def game_get_cards_from_players(game, guid):
        player = game.get_player(guid)
        if player:
            return {'cards': player.get_cards()}
        return {'message', 'Player not found'}
    return load_game(game_get_cards_from_players, guid)


@app.route('/game/players', methods=['GET'])
def get_players():
    def get_ordred_players(game):
        ordered_players = sorted(game.players.items(), key=lambda x: x[1].get_total(), reverse=True)
        players = []
        for player in ordered_players:
            players.append({player[0]: player[1].get_total()})
        return players
    return load_game(get_ordred_players)


@app.route('/game/get-count-by-suit', methods=['GET'])
def get_count_by_suit():
    def game_get_count_by_suit(game):
        return game.get_count_by_suits()
    return load_game(game_get_count_by_suit)


@app.route('/game/get-count-by-cards', methods=['GET'])
def get_count_by_cards():
    def game_get_count_by_cards(game):
        return game.get_count_by_cards()
    return load_game(game_get_count_by_cards)


@app.route('/game/shuffle', methods=['PUT'])
def shuffle():
    def game_shuffle(game):
        shuffle_cards(game.cards)
        return {'message': 'Cards shuffled'}
    return load_game(game_shuffle)


if __name__ == '__main__':
    app.run()