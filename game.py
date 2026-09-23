from hand import Hand
from deck import Deck

class Game:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.player_turn = True
        self.game_over = True

    def deal_init_cards(self):
        self.player_hand.add_card(self.deck.draw_card())
        self.dealer_hand.add_card(self.deck.draw_card())
        self.player_hand.add_card(self.deck.draw_card())
        self.dealer_hand.add_card(self.deck.draw_card())

    def hit(self):
        self.player_hand.add_card(self.deck.draw_card())

    def stand(self):
        self.player_turn = False

    def dealer_handler(self):
        if self.player_hand.check_bust():
            return
        while self.dealer_hand.get_hand_value() < 17:
            self.dealer_hand.add_card(self.deck.draw_card())

    def check_winner(self):
        player_bj = self.player_hand.check_blackjack()
        dealer_bj = self.dealer_hand.check_blackjack()

        if player_bj and dealer_bj:
            return 'Push'
        elif player_bj:
            return 'Player has a BLACKJACK!'
        elif dealer_bj:
            return 'Dealer has a BLACKJACK!'

        if self.player_hand.check_bust():
            return 'Dealer Win!'
        elif self.dealer_hand.check_bust():
            return 'Player Win!'

        player_hand_val = self.player_hand.get_hand_value()
        dealer_hand_val = self.dealer_hand.get_hand_value()

        if player_hand_val > dealer_hand_val:
            return 'Player Win!'
        elif player_hand_val < dealer_hand_val:
            return 'Dealer Win!'
        else:
            return 'Push'

    def reset_round(self):
        self.player_turn = True
        self.player_hand.cards.clear()
        self.dealer_hand.cards.clear()