# Pythonic Blackjack

A simple Blackjack game written in Python with a Tkinter GUI.

## Features

* Graphical user interface built with Tkinter
* Standard 52-card deck
* Cards are shuffled when the deck is created
* The deck is **not shuffled between rounds**
* Player actions:
  * Hit
  * Stand
* Dealer automatically draws cards until reaching at least 17
* Blackjack detection
* Bust detection
* Push detection
* Automatic round result
* Ability to start a new round after the previous one ends

## Rules

The game follows basic Blackjack rules:

* The player and dealer are initially dealt two cards.
* Number cards are worth their face value.
* Jack, Queen and King are worth 10.
* Ace is worth 1 or 11 depending on the hand.
* The player can Hit or Stand.
* The dealer must draw to 16 and stand on all 17s.
* If both player and dealer have Blackjack, the result is a push.
* If both hands have the same value, the result is a push.

## Project Structure

```text
blackjack/
├── card.py      # Card class
├── deck.py      # Deck creation, shuffling and drawing cards
├── hand.py      # Hand management and hand value calculation
├── game.py      # Blackjack game logic
├── gui.py       # Tkinter graphical interface
├── main.py      # Program entry point
└── README.md
```

### Classes

#### `Card`

Represents a single playing card and handles its value.

#### `Deck`

Creates and manages the deck of cards. Cards are shuffled when the deck is created and are drawn from the deck during the game.

#### `Hand`

Stores the cards belonging to the player or dealer and calculates the value of the hand.

#### `Game`

Contains the Blackjack game logic, including:

* dealing cards
* player actions
* dealer behaviour
* Blackjack detection
* checking the winner
* resetting the round

#### `BlackjackGUI`

Handles the graphical interface and communicates with the `Game` class.

## Running the Game

Make sure Python is installed, then run:

```bash
python main.py
```

The game window should open automatically.

## Technologies

* Python
* Tkinter

## Version

**v1.0**

First complete GUI version of Pythonic Blackjack.