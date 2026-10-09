import random
class Card:
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit
    def __str__(self):
        return(f"the card is {self.value} of {self.suit}")

Hearts5 = Card(5,"hearts")
print(Hearts5)

kingspades = Card(13,"spades")

print(kingspades)

jackdiamond = Card(11,"diamonds")

print(jackdiamond)

class Deck:
    def __init__(self):
        self.deck = []
        for i in range(4):
            suits = ["spades","hearts","clovers","diamonds"]
            for j in range(1,14):
                card = Card(j,suits[i])
                self.deck.append(card)
    def __str__(self):
        output = ""
        for i in self.deck:
            output += f"{i}\n"
        return output
    def drawcard(self):
        if len(self.deck) <= 0:
            return"You cant draw, there is nothing in the deck"
        else:
            return self.deck.pop(0)

    def shuffledeck(self):
        for i in range(52):
            rcard = random.randint(0,51)
            tempcard = self.deck[i]
            self.deck[i] = self.deck[rcard]
            self.deck[rcard] = tempcard






Casinodeck = Deck()

Casinodeck.shuffledeck()

print(Casinodeck)
for i in range(52):
    print(Casinodeck.drawcard())

print(Casinodeck.drawcard())