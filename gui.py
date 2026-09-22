from tkinter import *
from tkinter import ttk

class BlackjackGUI:
    def __init__(self, root):
        root.title("Pythonic Blackjack")
        root.geometry("550x350")

        content = ttk.Frame(root)
        blackjackLabel = ttk.Label(content, text="BLACKJACK")
        dealerLabel = ttk.Label(content, text="Dealer:")
        dealerCardsLabel = ttk.Label(content, text="6 | K | 5")
        dealerValLabel = ttk.Label(content, text="21")
        playerLabel = ttk.Label(content, text="Player:")
        playerCardsLabel = ttk.Label(content, text="Q | J")
        playerValLabel = ttk.Label(content, text="20")
        winnerLabel = ttk.Label(content, text="dealer_win")

        hitButton = ttk.Button(content, text="HIT")
        standButton = ttk.Button(content, text="STAND")

        content.grid(column=0, row=0, sticky=(N, S, E, W))
        
        blackjackLabel.grid(column=0, row=0, columnspan=3, pady=(0, 20))
        
        dealerLabel.grid(column=0, row=1, sticky=(E), padx=5, pady=10)
        dealerCardsLabel.grid(column=1, row=1, sticky=(E, W))
        dealerValLabel.grid(column=2, row=1, sticky=(W), padx=5)
        
        winnerLabel.grid(column=0, row=2, columnspan=3, pady=20)
        
        playerLabel.grid(column=0, row=3, sticky=(E), padx=5, pady=10)
        playerCardsLabel.grid(column=1, row=3, sticky=(E, W))
        playerValLabel.grid(column=2, row=3, sticky=(W), padx=5)
        
        hitButton.grid(column=0, row=4, sticky=(E), padx=5, pady=20)
        standButton.grid(column=2, row=4, sticky=(W), padx=5, pady=20)

        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
        content.columnconfigure(0, weight=1)
        content.columnconfigure(1, weight=3)
        content.columnconfigure(2, weight=1)
        
        content.rowconfigure(0, weight=1)
        content.rowconfigure(1, weight=1)
        content.rowconfigure(2, weight=1)
        content.rowconfigure(3, weight=1)
        content.rowconfigure(4, weight=1)

root = Tk()
BlackjackGUI(root)
root.mainloop()