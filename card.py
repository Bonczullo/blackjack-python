SUIT_TRANSLATION = {'Pik':'Spades', 'Kier':'Hearts', 'Trefl':'Clubs', 'Karo':'Diamonds'}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = SUIT_TRANSLATION.get(suit, suit)
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"