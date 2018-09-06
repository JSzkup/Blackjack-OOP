import random

class Card(object):
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f"{self.value} of {self.suit}")


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v)) # creates the instance of each card because (s, v) are passed

    def show(self):
        for c in self.cards:
            c.show()

    # shuffle algorithm that gives each card an equal weighing of each location inthe deck
    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

 
 
class Player(object):

    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()


    
deck = Deck()

# shuffles the deck and shows the whole hting
deck.shuffle()
# deck.show()

#pulls a card from the deck and shows it
# card = deck.draw()
# card.show()

bob = Player("Bob")
bob.draw(deck).draw(deck) # possible because of the "return self"
bob.showHand()





# A FUNCTION IS EQUAL TO ITS RETURN VALUE