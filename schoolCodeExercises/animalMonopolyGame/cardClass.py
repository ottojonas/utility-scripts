"""
Attributes: 
textToDisplay: string 
amount: integer 

Methods: 
constructor() 
getTextToDisplay()
getAmount()
"""


class Card:
    def __init__(self, textToDisplay, amount):
        self.textToDisplay = textToDisplay
        self.amount = amount

    def getTextToDisplay(self):
        return self.textToDisplay

    def getAmount(self):
        return self.amount

    def __str__(self):
        return f"Card: {self.textToDisplay}, Amount: {self.amount}"
