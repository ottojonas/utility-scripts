# Import the random module to generate random numbers
import random

# Main entry point of the script
if __name__ == "__main__":
    # Initialize score to 0
    score = int("0")
    # Loop 10 times to simulate 10 coin tosses
    for i in range(10):

        # Prompt the user to enter their choice (heads or tails)
        userChoice = input("Enter your choice")

        # Generate a random number between 1 and 2 to simulate a coin toss
        result = random.randint(1, 2)

        # If the random number is 1, the result is 'heads'
        if result == 1:
            result = "heads"

        # Otherwise, the result is 'tails'
        else:
            result = "tails"

        # Check if the result is 'heads'
        if result == "heads":
            # If the user's choice matches the result, they guessed correctly
            if userChoice == result:
                print("Congrats you got it right")
                score = score + 1
            # If the user's choice does not match, they guessed incorrectly
            else:
                print("It was heads you were wrong")

        # Check if the result is 'tails'
        if result == "tails":
            # If the user's choice matches the result, they guessed correctly
            if userChoice == result:
                print("Congrats you got it right")
                score = score + 1
            # If the user's choice does not match, they guessed incorrectly
            else:
                print("It was tails you were wrong")

    # After all iterations, print the total number of correct guesses
    print("Thank you for playing, you got", str(score), "correct guesses")
