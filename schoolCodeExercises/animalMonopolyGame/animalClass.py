"""
Attributes: 
name: string
currentLevel: int
cost: int 
L0: real 
L1: real 
L2: real 
L3: real 
imageLink: string 
setSquare: integer 
owned: string 

Methods
constructor() 
getCost() 
upgrade(player)
getCurrentLevel()
setOwned(player)
getOwned()
getAmountToCharge()
getName()
"""


class Animal:

    def __init__(self, randomNumber):
        self.animals = [
            ["Panda", 200],
            ["Koala", 400],
            ["Platypus", 150],
            ["Sloth", 70],
            ["Leemur", 25],
        ]
        self.owner = None
        self.currentLevel = 0
        self.name = self.animals[randomNumber][0]
        self.cost = self.animals[randomNumber][1]

    def __str__(self):
        return self.name

    def getCost(self):
        return self.cost

    def upgrade(self):
        self.currentLevel += 1

    def getCurrentLevel(self):
        return self.currentLevel

    def getOwner(self):
        return self.owner is not None

    def isAvailable(self):
        return self.owner is None

    def setOwner(self, playerName):
        self.owner = playerName

    def getAmountToCharge(self):
        return self.cost * (self.currentLevel + 1)

    def getName(self):
        return self.name
