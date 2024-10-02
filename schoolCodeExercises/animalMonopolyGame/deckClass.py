class Deck:
    def __init__(self):
        self.deck = []
        self.headPointer = 0

    def addCard(self, card):
        self.deck.append(card)

    def getCurrentCard(self):
        return self.deck[self.headPointer]

    def moveHeadPointer(self):
        self.headPointer += 1
        if self.headPointer == len(self.deck):
            self.headPointer = 0

    def pickDeck(self):
        pass
