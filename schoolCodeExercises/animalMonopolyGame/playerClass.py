"""
Attributes: 
playerName: string 
boardPosition: integer 
money: integer 

Methods: 
constructor() 
getPosition() 
setPosition(position)
getMoney()
setMoney(amount)
"""


class Player:
    def __init__(self, playerName):
        self.playerName = playerName
        self.boardPosition = 0
        self.money = 2000
        self.animalsOwned = []

    def getPosition(self):
        return self.boardPosition

    def setPosition(self, position, board):
        self.boardPosition = position
        animal = board.getAnimalAtPosition(position)
        if animal is not None and animal.isAvailable():
            self.buyAnimal(animal)

    def getMoney(self):
        return self.money

    def setMoney(self, amount):
        self.money = amount

    def buyAnimal(self, animal):
        purchase = input(f"Do you want to purchase {animal.name}? (yes/no): ")
        if purchase.lower() == "yes":
            if self.money >= animal.cost:
                self.money -= animal.cost
                self.animalsOwned.append(animal)
                animal.setOwner(self)
            else:
                print("You don't have the funds to buy this animal.")
        else:
            print(f"You have chosen not to purchase {animal.name}")
