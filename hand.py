class Hand:
    def __init__(self):
        self.cards = []

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return " | ".join([str(card) for card in self.cards])

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        aces = 0
        for card in self.cards:
            if card.rank == 'Ace':
                value += 11
                aces += 1
            elif card.rank in ['Jack', 'Queen', 'King']:
                value += 10
            else:
                value += int(card.rank)
        while value > 21 and aces > 0:
            aces -= 1
            value -= 10
        return value

    def check_blackjack(self):
        return len(self) == 2 and self.get_value() == 21

    def check_bust(self):
        return self.get_value() > 21