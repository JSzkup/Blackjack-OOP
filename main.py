# oop blackjack

## stretch goals ##
# add a money/betting system
# ui

import random
from random import shuffle

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

    # debugging function
    def show(self):
        print(f"{self.rank} of {self.suit}")

    def __str__(self):
        return self.rank + " of " + self.suit

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

    def getValue(self):
        self.value = 0
        for card in self.hand:
            self.value += RANKS[card.getRank()]
            if str(card.getRank()) == "Ace":
                if self.value <= 11:
                    self.value += 10
        
        return self.value

    def showValue(self):
        self.shownVal = self.getValue()
        print(f"Card value totals: {self.shownVal}")

    # debugging function
    def showHand(self):
        for card in self.hand:
            card.show()

    def draw(self, deck):
        self.hand.append(deck.drawCard())

        return self

    def bust(self):
        if self.getValue() > 21:

            return True
        
    def __str__(self):
        # a string to print the player or dealers hand
        print(self.hand)
        print(f"Hand value is {self.value}")

# initializing objects
deck = Deck()
player = Hand()
dealer = Hand()

def main():
    gameIsPlaying = True

    # welcome the player
    print("Welcome to BlackJack")
    ## explain basic rules if they dont know how to play
    tutorial = input("Do you know how to play BlackJack?: (Yes/No)\n")
    if tutorial.lower() == 'no':
            print("The goal of the game is to reach a score (=sum of the cards) as high as possible but not more than 21. \n A Blackjack (Ace and a card whose value is 10) beats all other combination of cards.\n If the final sum is higher than the sum of the dealer, the player wins.")
            print()
    print()

    turn = player

    # drawing 2 initial cards for the player
    # 1 for the dealer
    player.draw(deck).draw(deck)
    dealer.draw(deck)
    
    # showing the full hands to the player
    # TODO hide one card of the dealer & dont show their value
    print("Your full hand is:")
    player.showHand()
    player.getValue()
    player.showValue()

    print()
    
    print("The dealers hand is:")
    dealer.showHand()
    print("[Hidden Card]")
    dealer.getValue()
    print("Total card value unknown")
    dealer.draw(deck)

    while gameIsPlaying:
        # player decides whether to stand or hit based off of the total of their current 2 cards
        if turn == player:
            print()
            print("What Would you like to do:")
            print("Hit")
            print("Stay")
            print()

            choice = input()
            print()

            if choice.lower() == "hit":
                player.draw(deck)
                if player.bust():
                    print("remove this later: YOU'RE BUST")
                    gameIsPlaying = False
            else:
                turn = dealer # TODO move this
            
            print("Your full hand is:")
            player.showHand()
            player.getValue()
            player.showValue()

        # dealer ai
        # dealer will draw a card if their total value is under 13
        if turn == dealer:
            print()
            print("The dealer will now play")
            print()
            while dealer.getValue() < 21:
                if dealer.getValue() < 13:
                    dealer.draw(deck)
                    if dealer.bust():
                        print("remove this later: DEALER BUST")
                        gameIsPlaying = False
                else:
                    # dealer will randomly pull a new card anyway (> 13) so it's not boring
                    wildCard = random.randint(0, 1)

                    if wildCard == 1:
                        dealer.draw(deck)
                        if dealer.bust():
                            print("remove this later: DEALER BUST")
                            gameIsPlaying = False
            
            print("The Dealers hand is:")
            dealer.showHand()
            dealer.getValue()
            dealer.showValue()

            turn = 0        

    print("Game has ended")        

    # TODO comparing scores if no one went bust
    # TODO        



if __name__ == "__main__":
    main()


#### https://en.wikipedia.org/wiki/Playing_cards_in_Unicode ####
# TODO possibly use a json file of all cards to pull from for deck
# could label each card individually and pull from that using a string == string
