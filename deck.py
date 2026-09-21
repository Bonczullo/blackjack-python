import random
from card import Card

SUITS = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(rank, suit))
        self.shuffle_deck()

    def __str__(self):
        return "\n".join([str(card) for card in self.cards])

    def __len__(self):
        return len(self.cards)

    def draw_card(self):
        if not self.cards:
            self.reset_deck()
        return self.cards.pop()

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def reset_deck(self):
        self.cards.clear()
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(rank, suit))
        self.shuffle_deck()