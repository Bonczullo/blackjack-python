from tkinter import *
from tkinter import ttk

from card import Card
from deck import Deck
from hand import Hand
from game import Game
from gui import BlackjackGUI

if __name__ == "__main__":
    root = Tk()
    BlackjackGUI(root)
    root.mainloop()