# Board is an array of animal objects - Each square is an animal except the start and miss a turn square
import random

from animalClass import Animal


class Board:
    def __init__(self):
        self.board = []
        self.createBoard()

    def createBoard(self):
        self.board.append("Start")
        for i in range(12):
            randomNumber = random.randint(0, 4)
            self.board.append(Animal(randomNumber))
        self.board.append("Miss a Turn")
        for i in range(12):
            randomNumber = random.randint(0, 4)
            self.board.append(Animal(randomNumber))

    def getAnimalAtPosition(self, position):
        square = self.board[position]
        if isinstance(square, Animal):
            return square
        else:
            return None

    def __str__(self):
        boardString = ""
        for animal in self.board:
            boardString += str(animal) + " "
        boardString += "\n"
        return boardString
