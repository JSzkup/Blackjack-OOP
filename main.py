# oop blackjack


# going to be OOP
# card values listed in a dictionary
# try and have "A" be dynamic and be a 1 or 11 based off of your cards

## stretch goals ##
# add a money/betting system
# ui
# simulate an actual deck with the right amount of each card

import random
from random import shuffle

CARDS = {
    "K": 10,
    "Q": 10,
    "J": 10,
    "10":10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "A": 1,
}

# Possibly make a randomly generated list of cards and push them to the "bottom" of the deck
# TODO check if stacks can be pushed to the back of the stack
# push -> on stack
# pop <- off stack

class Deck:
    deck = []
    for i in range(0, 52):
        i = random.choice(CARDS.keys())
        deck.push (i)

class BlackJack:

    def __init_(self):
        self.gameIsPlaying = True 

    def tutorial(self):
        print("Here is how to play Blackjack...")

    def gameStatus(self, playerHand, dealerHand):
        print("Here are your cards")
        # TODO show not only the running total of cards, but the cards themselves

        print("Here are the dealers cards")


        print("What Would you like to do:")
        print("H - Hit")
        print("S - Stay")
        print()

        return choice

    # def newCard(self):
    #     return random.choice(CARDS.keys())

    def showCards(self):

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
