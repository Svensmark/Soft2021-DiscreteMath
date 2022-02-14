import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def getCardValue(self):
        if(self.suit == "Spades"):
            return self.value
        if(self.suit == "Hearts"):
            return self.value + 13
        if(self.suit == "Clubs"):
            return self.value + 26
        if(self.suit == "Diamonds"):
            return self.value + 39        

    def __repr__(self):
        return (str(self.suit) + " " + str(self.value))


class Deck:
    def __init__(self):
        self.cards = []

    def fillDeck(self):
        if not self.cards:
            suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
            for suit in suits:
                for value in range(13):
                    card = Card(suit, value+1)
                    self.cards.append(card)

    def shuffleDeck(self):
        random.shuffle(self.cards)

    def sortDeck(self):
        for i in range(1, len(self.cards)):
            key = self.cards[i]
            j = i-1
            while j >=0 and key.getCardValue() < self.cards[j].getCardValue():
                    self.cards[j+1] = self.cards[j]
                    j -= 1
            self.cards[j+1] = key


deck = Deck()
#print(deck.cards)
deck.fillDeck()
print("")
print("")
print("Deck will now be filled with a full deck of cards:")
print(deck.cards)
deck.shuffleDeck()
print("")
print("")
print("Deck is now shuffled, and has the following array:")
print(deck.cards)
print("")
print("")
print("Deck will now be sorted:")
deck.sortDeck()
print(deck.cards)