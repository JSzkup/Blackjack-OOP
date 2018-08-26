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
        # TODO might need to become a dict anyway to store the value
    
def SUITS(): 
    return [ "Clubs", "Diamonds", "Hearts", "Spades" ]

class Card:
    # Each card made with its own rank and suite

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + " of " + self.suit
        # TODO make this work with a dictionary and its keys


class Deck:
    # every card is put into a deck and shuffled

    def __init__(self):
        self.contents = []
        self.contents = [Card(rank, suit) for rank in RANKS() for suit in SUITS()]
        random.shuffle(self.contents)

        return self.contents

class Hand:

    def __init__(self):
        self.hand = []

    def addCard(self, card):
        self.hand.append(card)

    def getValue(self):
        value = 0
        # TODO add up all the cards in the hand

        return value

    def bust(self):
        # determines if the hand is over 21 and ends the game

    def __str__(self):
       # a string to print the player or dealers hand


class Player:

class Dealer:

class BlackJack: # might need to put all of this in main

    def __init_(self):
        self.gameIsPlaying = True 

    def tutorial(self):
        print("Here is how to play Blackjack...")

        print("Here are the dealers cards")


    def choice(): # probably needs to be in main
        print("What Would you like to do:")
        print("H - Hit")
        print("S - Stay")
        print()

        return choice

    # def newCard(self):
    #     return random.choice(CARDS.keys())

    def dealerAI(self):
        # will the dealer decide to H, S, DD, S
        # Base this off of how high their number is



############################
#Write how the program is going to work here first, with names of functions ill create later
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

