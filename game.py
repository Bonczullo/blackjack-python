from hand import Hand
from deck import Deck

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.player_turn = True

    def deal_init_cards(self):
        self.player_hand.add_card(self.deck.draw_card())
        self.dealer_hand.add_card(self.deck.draw_card())
        self.player_hand.add_card(self.deck.draw_card())
        self.dealer_hand.add_card(self.deck.draw_card())

    def check_init_blackjack(self):
        player_bj = self.player_hand.check_blackjack()
        dealer_bj = self.dealer_hand.check_blackjack()
        if player_bj and not dealer_bj:
            return 'player_bj'
        elif not player_bj and dealer_bj:
            return 'dealer_bj'
        elif player_bj and dealer_bj:
            return 'both_bj'
        else:
            return 'no_bj'

    def hit(self):
        if not self.player_turn:
            return
        self.player_hand.add_card(self.deck.draw_card())
        if self.player_hand.check_bust():
            self.player_turn = False

    def stand(self):
        if not self.player_turn:
            return
        self.player_turn = False

    def dealer_handler(self):
        if self.player_turn or self.player_hand.check_bust():
            return
        while self.dealer_hand.get_value() < 17:
            self.dealer_hand.add_card(self.deck.draw_card())

    def check_winner(self):
        if self.player_turn:
            return
        blackjack = self.check_init_blackjack()
        player_hand_val = self.player_hand.get_value()
        dealer_hand_val = self.dealer_hand.get_value()
        if blackjack == 'player_bj':
            return 'player_win'
        elif blackjack == 'dealer_bj':
            return 'dealer_win'
        elif blackjack == 'both_bj':
            return 'push'
        if self.player_hand.check_bust():
            return 'dealer_win'
        elif self.dealer_hand.check_bust():
            return 'player_win'
        if player_hand_val > dealer_hand_val:
            return 'player_win'
        elif player_hand_val < dealer_hand_val:
            return 'dealer_win'
        else:
            return 'push'