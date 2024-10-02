import random  # Import the random module for selecting a random word


def getWord(wordList):
    # Selects and returns a random word from the provided word list
    return random.choice(wordList)


def gameState(word, guessedLetters):
    # Displays the current state of the word with guessed letters and underscores for unguessed letters
    displayedWord = "".join(
        [letter if letter in guessedLetters else "_" for letter in word]
    )
    print(f"word {displayedWord}")
    # Displays the letters that have been guessed so far
    print(f"Guessed letters {" ".join(guessedLetters)}")


def getGuess(guessedLetters):
    # Continuously prompts the user to enter a letter until they enter one that hasn't been guessed yet
    while True:
        guess = input("Enter letter: ")
        if guess not in guessedLetters:
            return guess  # Return the new guess
        else:
            print(
                "You have already used that letter"
            )  # Notify the user if the letter was already guessed


def updateGame(word, guessedLetters, guess):
    # Updates the game state based on the user's guess
    isCorrectGuess = False
    if guess in word:
        if guess not in guessedLetters:
            guessedLetters.append(guess)  # Add the correct guess to the guessed letters
        isCorrectGuess = True
    elif guess not in word and guess in guessedLetters:
        print(
            "You have already used that letter"
        )  # Notify the user if the letter was already guessed
    else:
        if guess not in guessedLetters:
            guessedLetters.append(
                guess
            )  # Add the incorrect guess to the guessed letters
    return (
        guessedLetters,
        isCorrectGuess,
    )  # Return the updated guessed letters and whether the guess was correct


def isGameOver(word, guessedLetters, livesLeft):
    # Checks if the game is over either by running out of lives or guessing all letters in the word
    if livesLeft == 0 or set(word) == set(guessedLetters):
        return True
    return False


def main():
    # Main function to run the hangman game
    wordList = [
        "iguana",
        "chameleon",
        "salamandar",
        "komodo",
        "gecko",
        "lounge",
    ]  # List of possible words
    word = getWord(wordList)  # Select a random word from the list
    guessedLetters = []  # Initialize an empty list for guessed letters
    maxAttempts = 10  # Set the maximum number of attempts
    livesLeft = maxAttempts  # Initialize lives left to the maximum attempts

    # Game loop that continues until the game is over
    while not isGameOver(word, guessedLetters, livesLeft):
        gameState(word, guessedLetters)  # Display the current game state
        guess = getGuess(guessedLetters)  # Get a new guess from the user
        guessedLetters, isCorrectGuess = updateGame(
            word, guessedLetters, guess
        )  # Update the game state with the new guess
        if not isCorrectGuess:
            livesLeft -= 1  # Decrease lives left if the guess was incorrect
            print(f"You lost a life, you have {livesLeft} lives left")
    if set(word) == set(guessedLetters):
        print("You win")  # Print win message if all letters are guessed
    else:
        print("You lose")  # Print lose message if lives run out


main()  # Run the main function to start the game
