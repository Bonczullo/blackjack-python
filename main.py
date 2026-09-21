from card import Card
from deck import Deck
from hand import Hand
from game import Game

if __name__ == "__main__":
    game = Game()
    while True:
        game.play_round()
        game.reset_round()
        result = input("Czy chcesz zagrać ponownie? y/n:")
        if result == 'n':
            break