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

    def hit(self):
        if not self.player_turn:
            return
        self.player_hand.add_card(self.deck.draw_card())
        if self.player_hand.check_bust() or self.player_hand.get_hand_value() == 21:
            self.player_turn = False

    def stand(self):
        if not self.player_turn:
            return
        self.player_turn = False

    def player_handler(self):
        while self.player_turn:
            action = input("Akcja (h - hit, s - stand):")
            if action == 'h':
                self.hit()
                print(f"Karty gracza: {self.player_hand} -> {self.player_hand.get_hand_value_str()}")
            elif action == 's':
                self.stand()
            else:
                print("Niepoprawna akcja! Wpisz 'h' lub 's'.")

    def dealer_handler(self):
        if self.player_turn or self.player_hand.check_bust():
            return
        while self.dealer_hand.get_hand_value() < 17:
            self.dealer_hand.add_card(self.deck.draw_card())

    def check_winner(self):
        player_bj = self.player_hand.check_blackjack()
        dealer_bj = self.dealer_hand.check_blackjack()

        if player_bj and dealer_bj:
            return 'push'
        elif player_bj:
            return 'player_win'
        elif dealer_bj:
            return 'dealer_win'

        if self.player_hand.check_bust():
            return 'dealer_win'
        elif self.dealer_hand.check_bust():
            return 'player_win'

        player_hand_val = self.player_hand.get_hand_value()
        dealer_hand_val = self.dealer_hand.get_hand_value()

        if player_hand_val > dealer_hand_val:
            return 'player_win'
        elif player_hand_val < dealer_hand_val:
            return 'dealer_win'
        else:
            return 'push'

    def play_round(self):
        self.deal_init_cards()
        print(f"Karty gracza: {self.player_hand} -> {self.player_hand.get_hand_value_str()}")
        print(f"Dealer: {self.dealer_hand.cards[0]} -> {self.dealer_hand.cards[0].get_card_value()}")
        if self.player_hand.check_blackjack() or self.dealer_hand.check_blackjack():
            self.player_turn = False
            print(f"Karty dealera: {self.dealer_hand}  -> {self.dealer_hand.get_hand_value()}")
            print('BLACKJACK!')
        else:
            self.player_handler()
            self.dealer_handler()
            print(f"Dealer: {self.dealer_hand}  -> {self.dealer_hand.get_hand_value()}")
        print(self.check_winner())

    def reset_round(self):
        self.player_turn = True
        self.player_hand.cards.clear()
        self.dealer_hand.cards.clear()