# oop blackjack

## stretch goals ##
# add a money/betting system
# ui

import random
from random import shuffle

# initializing constants as functions
def RANKS():
    return [
    "Ace":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "10":10,
    "Jack":10,
    "Queen":10,
    "King":10
    ]
    
def SUITS(): 
    return [ "Clubs", "Diamonds", "Hearts", "Spades" ]

class Card:
    # Each card made with its own rank and suite

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_rank(self):
        return self.rank

    def __str__(self):
        return self.rank + " of " + self.suit
        # TODO make this work with a dictionary and its keys


class Deck:
    # every card is put into a deck and shuffled

    def __init__(self):
        self.cards = []
        self.cards = [Card(rank, suit) for rank in RANKS() for suit in SUITS()]
        random.shuffle(self.cards)

        return self.cards

    def shuffle(self):
        random.shuffle(self.cards)

class Hand:

    def __init__(self):
        self.hand = []

    def addCard(self, card):
        self.hand.append(card)

    def getValue(self):
        value = 0
        for Card in self.hand:
            value += RANKS[card.get_rank()]
            if str(card.get_rank()) == "Ace":
                if value <= 11:
                    value += 10

        return value
        # TODO check for bust hands elsewhere

    def __str__(self):
       # a string to print the player or dealers hand


class Player:

    def choice(): # probably needs to be in main
        print("What Would you like to do:")
        print("H - Hit")
        print("S - Stay")
        print()

        return choice

class Dealer:

    def ai():


class BlackJack: # might need to put all of this in main

    def __init_(self):
        self.gameIsPlaying = True 

############################
# Write how the program is going to work here first, with names of functions ill create later
############################
def main():
        # welcome the 
        print("Welcome to BlackJack")
        ## explain basic rules if they dont know how to play
        tutorial = input("Do you know how to play BlackJack?: ")
        if tutorial.lower() == 'y':
            print("The rules are..........")
            print()


        # deals 2 cards to the player and 2 to the dealer, the dealer having one card face down and one face up

    while self.gameIsPlaying:
        # player decides whether to stand, hit, surrender, double down, or split based off of the total of their current 2 cards
        # after the player decides to stay, the dealer then decides whether or not to hit
        # whoever has the higher number in the end wins, if you go over 21 you lose

if __name__ == "__main__":
    main()


# http://ascii.co.uk/art/cards
# https://en.wikipedia.org/wiki/Playing_cards_in_Unicode
# https://www.asciiart.eu/miscellaneous/playing-cards

