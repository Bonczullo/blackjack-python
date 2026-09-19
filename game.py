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

        if self.check_init_blackjack() != 'no_bj':
            self.player_turn = False

    def check_init_blackjack(self):
        player_bj = self.player_hand.check_blackjack()
        dealer_bj = self.dealer_hand.check_blackjack()
        if player_bj and not dealer_bj:
            return 'player_blackjack'
        elif not player_bj and dealer_bj:
            return 'dealer_blackjack'
        elif player_bj and dealer_bj:
            return 'both_bj'
        else:
            return 'no_bj'

    def hit(self):
        if not self.player_turn:
            return
        self.player_hand.add_card(self.deck.draw_card())
        if self.player_hand.check_bust() or self.player_hand.get_value() == 21:
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

    def player_handler(self):
        while self.player_turn:
            action = input("Akcja (h - hit, s - stand):")
            if action == 'h':
                self.hit()
                print(f"Karty gracza: {self.player_hand} -> {self.player_hand.get_value_str()}")
            elif action == 's':
                self.stand()
            else:
                print("Niepoprawna akcja! Wpisz 'h' lub 's'.")

    def check_winner(self):
        if self.player_turn:
            return
        player_hand_val = self.player_hand.get_value()
        dealer_hand_val = self.dealer_hand.get_value()
        
        player_bj = self.player_hand.check_blackjack()
        dealer_bj = self.dealer_hand.check_blackjack()

        if player_bj and not dealer_bj:
            return 'player_win'
        elif not player_bj and dealer_bj:
            return 'dealer_win'
        elif player_bj and dealer_bj:
            return 'push'
        elif self.player_hand.check_bust():
            return 'dealer_win'
        elif self.dealer_hand.check_bust():
            return 'player_win'
        elif player_hand_val > dealer_hand_val:
            return 'player_win'
        elif player_hand_val < dealer_hand_val:
            return 'dealer_win'
        else:
            return 'push'

    def play_round(self):
        self.deal_init_cards()
        blackjack = self.check_init_blackjack()
        print(f"Karty gracza: {self.player_hand} -> {self.player_hand.get_value_str()}")
        print(f"Karta dealera: {self.dealer_hand.cards[0]}")
        if blackjack != 'no_bj':
            print(f"Karta dealera: {self.dealer_hand}  -> {self.dealer_hand.get_value()}")
            print(blackjack)
            print(self.check_winner())
            return
        self.player_handler()
        self.dealer_handler()
        print(f"Dealer: {self.dealer_hand}  -> {self.dealer_hand.get_value()}")
        print(self.check_winner())
        