SUIT_TRANSLATION = {'Pik':'Spades', 'Kier':'Hearts', 'Trefl':'Clubs', 'Karo':'Diamonds'}

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = SUIT_TRANSLATION.get(suit, suit)
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def get_card_value(self):
        if self.rank == 'Ace':
            return 11
        elif self.rank in ['Jack', 'Queen', 'King']:
            return 10
        else:
            return int(self.rank)

    def get_card_value_str(self):
        if self.rank == 'Ace':
            return '1/11'
        return str(self.get_card_value())