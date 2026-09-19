from card import Card
from deck import Deck
from hand import Hand
from game import Game

# deck1 = Deck()
# hand1 = Hand()
# for i in range(2):
#     hand1.add_card(deck1.draw_card())
# print(hand1)
# print(hand1.get_value())

game = Game()
game.play_round()

# game.deal_init_cards()
# print(f"Karty gracza: {game.player_hand} -> {game.player_hand.get_value()}")
# print(f"Karta dealera: {game.dealer_hand.cards[0]}")
# game.check_init_blackjack()
# while game.player_turn:
#     action = input("Akcja:")
#     if action == 'hit':
#         game.hit()
#         print(f"Karty gracza: {game.player_hand} -> {game.player_hand.get_value()}")
#     elif action == 'stand':
#         game.stand()
#     else:
#         print("Co ty kurwa piszesz ziomek")
# game.dealer_handler()
# print(f"Dealer: {game.dealer_hand}  -> {game.dealer_hand.get_value()}")
# print(game.check_winner())

