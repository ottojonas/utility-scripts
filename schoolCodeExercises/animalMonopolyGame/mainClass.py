import random

from boardClass import Board
from playerClass import Player


class Main:
    def __init__(self, players):
        self.players = players
        self.board = Board()
        self.playGame()

    def playGame(self):
        while True:
            for player in self.players:
                self.takeTurn(player)

    def takeTurn(self, player):
        roll = self.rollDice()
        print(f"{player.playerName} rolled {roll}")

    @staticmethod
    def rollDice():
        diceOne = random.randint(1, 6)
        diceTwo = random.randint(1, 6)
        if diceOne == diceTwo:
            pass

    def printBoard(self):
        print(self.board)

    def offerAnimalToPlayers(self, animal):
        for player in self.players:
            if player.buyAnimal(animal):
                print(f"{player.playerName} has chosen to purchase {animal}")


players = []
for i in range(4):
    playerName = input("Enter your name: ")
    players.append(Player(playerName))
myGame = Main(players)
myGame.printBoard()
