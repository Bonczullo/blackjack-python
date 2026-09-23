from tkinter import *
from tkinter import ttk
from game import Game

class BlackjackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pythonic Blackjack")
        self.root.geometry("550x350")

        self.game = Game()

        self.dealerCards = StringVar()
        self.dealerVal = StringVar()

        self.playerCards = StringVar()
        self.playerVal = StringVar()

        self.winner = StringVar()

        self.info = StringVar()

        self.build_GUI()

    def build_GUI(self):
        self.info.set("Press 'START' to deal the cards")
        content = ttk.Frame(self.root)
        content.grid(column=0, row=0, sticky=(N, S, E, W))
        # Blackjack label
        ttk.Label(content, text="Pythonic BLACKJACK").grid(column=0, row=0, columnspan=3)
        # Dealer
        ttk.Label(content, text="Dealer:").grid(column=0, row=1, sticky=(E))
        ttk.Label(content, textvariable=self.dealerCards).grid(column=1, row=1, sticky=(E, W))
        ttk.Label(content, textvariable=self.dealerVal).grid(column=2, row=1, sticky=(W))
        # Winner
        ttk.Label(content, textvariable=self.winner).grid(column=0, row=2, columnspan=3)
        # Info
        ttk.Label(content, textvariable=self.info).grid(column=0, row=3, columnspan=3)
        # Player
        ttk.Label(content, text="Player:").grid(column=0, row=4, sticky=(E), padx=5)
        ttk.Label(content, textvariable=self.playerCards).grid(column=1, row=4, sticky=(E, W))
        ttk.Label(content, textvariable=self.playerVal).grid(column=2, row=4, sticky=(W))
        # Buttons
        ttk.Button(content, text="HIT", command=self.hit).grid(column=0, row=5, sticky=(E))
        ttk.Button(content, text="START", command=self.start).grid(column=1, row=5)
        ttk.Button(content, text="STAND", command=self.stand).grid(column=2, row=5, sticky=(W))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        content.columnconfigure(0, weight=1)
        content.columnconfigure(1, weight=3)
        content.columnconfigure(2, weight=1)
        
        content.rowconfigure(0, weight=1)
        content.rowconfigure(1, weight=1)
        content.rowconfigure(2, weight=1)
        content.rowconfigure(3, weight=1)
        content.rowconfigure(4, weight=1)
        content.rowconfigure(5, weight=1)

    def hit(self):
        if self.game.game_over or not self.game.player_turn:
            return
        self.game.hit()
        self.playerCards.set(self.game.player_hand)
        self.playerVal.set(self.game.player_hand.get_hand_value_str())
        if self.game.player_hand.check_bust() or self.game.player_hand.get_hand_value() == 21:
            self.stand()

    def stand(self):
        if self.game.game_over or not self.game.player_turn:
            return
        self.game.stand()
        self.game.dealer_handler()
        self.dealerCards.set(self.game.dealer_hand)
        self.dealerVal.set(self.game.dealer_hand.get_hand_value_str())
        self.winner.set(self.game.check_winner())
        self.info.set("Press 'START' to play again!")
        self.game.game_over = True

    def start(self):
        if not self.game.game_over:
            return
        self.info.set("")
        self.winner.set("")
        self.game.game_over = False
        self.game.reset_round()
        self.game.deal_init_cards()
        self.dealerCards.set(self.game.dealer_hand.cards[0])
        self.dealerVal.set(self.game.dealer_hand.cards[0].get_card_value_str())
        self.playerCards.set(self.game.player_hand)
        self.playerVal.set(self.game.player_hand.get_hand_value_str())
        player_bj = self.game.player_hand.check_blackjack()
        dealer_bj = self.game.dealer_hand.check_blackjack()
        if player_bj or dealer_bj:
            self.game.player_turn = False
            self.game.game_over = True
            self.winner.set(self.game.check_winner())
            self.dealerCards.set(self.game.dealer_hand)
            self.dealerVal.set(self.game.dealer_hand.get_hand_value_str())
            self.info.set("Press 'START' to play again!")