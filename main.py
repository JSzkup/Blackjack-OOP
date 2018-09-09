# oop blackjack

## stretch goals ##
# add a money/betting system
# ui

import random
from random import shuffle
# TODO Import Logs?

gameIsPlaying = True

# initializing constants as functions
RANKS = { "Ace":1, "2":2, "3":3, "4":4, "5":5, "6":6, 
"7":7, "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King":10 }
    
SUITS = ("Clubs", "Diamonds", "Hearts", "Spades")

class Card(object):
    # Each card made with its own rank and suite
    # TODO if usung icons to represent cards take color into account RED/BLACK

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.hidden = False

    def getRank(self):
        return self.rank

    def getSuite(self):
        return self.suit

    def hide_card(self):
        self.hidden = True

    def reveal_card(self):
        self.hidden = False    

    # debugging function
    def show(self):
        print(f"{self.rank} of {self.suit}")

    def __str__(self):
        if self.hidden:
            return "[X]"
        else:
            return self.rank + " of " + self.suit
        # TODO make this work with a dictionary and its keys


class Deck(object):
    # every card is put into a deck and shuffled

    def __init__(self):
        self.cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
        random.shuffle(self.cards)

    # debugging function
    def show(self):
        for c in self.cards:
            c.show()

    def drawCard(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

class Hand(object):
    # The cards from the deck are pulled from and put into the dealer/players hand

    def __init__(self):
        self.hand = []

    # def addCard(self, card):
    #     self.hand.append(card)

    def getValue(self):
        self.value = 0
        for card in self.hand:
            self.value += RANKS[card.getRank()]
            if str(card.getRank()) == "Ace":
                if self.value <= 11:
                    self.value += 10
        
        print(f"Card value totals:  {self.value}")

        return self.value

    # debugging function
    def showHand(self):
        for card in self.hand:
            card.show()

    def draw(self, deck):
        self.hand.append(deck.drawCard())

        return self

    # TODO check for bust hands
    #def bust():
    #    
    #    return bust
    #    # Might do this in main()/Player instead

    def __str__(self):
        print(self.hand)
        print(f"Hand value is {self.value}")
       # a string to print the player or dealers hand

# class Dealer(object):
#     # The dealers choices for whether or not they'll hit/stay
#     # wont actually be dealing the cards here
# 
#     def __init__(self, dHand):
#         self.dHand = []
# 
#     # TODO dealer ai
#     # def ai():

deck = Deck()
player = Hand()
dealer = Hand()

def main():
    # welcome the player
    print("Welcome to BlackJack")
    ## explain basic rules if they dont know how to play
    tutorial = input("Do you know how to play BlackJack?: (Yes/No)\n")
    if tutorial.lower() == 'no':
            print("The rules are..........")
            print()
    print()

    turn = player
    player.draw(deck).draw(deck)
    dealer.draw(deck).draw(deck)
    
    print("Your full hand is:")
    player.showHand()
    player.getValue()
    print()
    print("The dealers hand is:")
    dealer.showHand()
    dealer.getValue()

    # deals 2 cards to the player and 2 to the dealer, the dealer having one card face down and one face up

    while gameIsPlaying:
        #     # player decides whether to stand, hit, surrender, double down, or split based off of the total of their current 2 cards
        if turn == player:
            print()
            print("What Would you like to do:")
            print("Hit")
            print("Stay")
            print()

            choice = input()

            if choice.lower() == "hit":
                player.draw(deck)
            else:
                turn = dealer
            
            print("Your full hand is:")
            player.showHand()

            player.getValue()

        # if turn == dealer:



        #     # after the player decides to stay, the dealer then decides whether or not to hit
        #     # whoever has the higher number in the end wins, if you go over 21 you lose
 

if __name__ == "__main__":
    main()


#### https://en.wikipedia.org/wiki/Playing_cards_in_Unicode ####
# TODO possibly use a json file of all cards to pull from for deck
# could label each card individually and pull from that using a string == string
