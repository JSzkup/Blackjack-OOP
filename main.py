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

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.hidden = False

    def getRank(self):
        return self.rank

    def getSuite(self):
        return self.suit

    def show(self):
        print(f"{self.rank} of {self.suit}")

class Deck(object):
    # every card is put into a deck and shuffled

    def __init__(self):
        self.cards = [Card(rank, suit) for rank in RANKS for suit in SUITS]
        random.shuffle(self.cards)

    def show(self):
        for c in self.cards:
            c.show()

    # takes a card off the top of the deck
    def drawCard(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)

class Hand(object):
    # The cards from the deck are pulled from and put into the dealer/players hand

    def __init__(self):
        self.hand = []

    # iterates through cards and adds the rank of each card to variable "value"
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

    def showHand(self):
        for card in self.hand:
            card.show()

    # appends the popped card to the player/dealers hand
    def draw(self, deck):
        self.hand.append(deck.drawCard())

        return self

    def bust(self):
        if self.getValue() > 21:

            return True

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

    # TODO try to remove this without breaking anything
    turn = player

    # drawing 2 initial cards for the player
    # 1 for the dealer
    player.draw(deck).draw(deck)
    dealer.draw(deck)
    
    # showing the full hands to the player
    print("Your full hand is:")
    player.showHand()
    player.getValue()
    player.showValue()

    print()
    
    # pretending a card is actually drawn and hidden to reduce computations
    print("The dealers hand is:")
    dealer.showHand()
    print("[Hidden Card]")
    dealer.getValue()
    print("Total card value unknown")
    dealer.draw(deck)

    while gameIsPlaying:
        # player decides whether to stand or hit based off of the total of their current 2 cards
        
        # TODO might be able to break this up into 2 classes to shorten main()
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
        if turn == dealer: # TODO possibly change this to else: to reduce variables
            print()
            print("The dealer will now play")
            print()
            while dealer.getValue() < 17:
                if dealer.getValue() < 11:
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

            gameIsPlaying = False        

    print()
    print("Game has ended")
    print()

    endPl = player.getValue()
    endDl = dealer.getValue()

    # displays the winner to the user
    if endPl > endDl and not player.bust():
        print(f"The player has won with {endPl} points over the dealers {endDl} points!")
    elif endPl < endDl and not dealer.bust():
        print(f"The dealer has won with {endDl} points over the players {endPl} points!")
    elif dealer.bust():
        print(f"The dealer is Bust and the player wins!")
    elif endPl == endDl and not dealer.bust() or not player.bust():
        print(f"It's a tie at {endPl} points.")
    else:
        print(f"The player is Bust and loses with {endPl} points.")
    



if __name__ == "__main__":
    main()


#### https://en.wikipedia.org/wiki/Playing_cards_in_Unicode ####
# TODO test if ACE really does what it's supposed to do      
# could label each card individually and pull from that using a string == string
