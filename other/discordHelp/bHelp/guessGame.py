import random

print("Welcome to my guessing game")

while True:
    # Generate a random number between 1 and 10
    random_number = random.randint(1, 10)

    # Ask the user to guess the number
    user_guess = int(input("Guess a number between 1 and 10: "))

    # Check if the user's guess is correct and provide feedback
    if user_guess == random_number:
        print("Correct, you win!")
    else:
        print("Wrong Number! The number was", random_number)

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break  # Exit the loop if the user does not want to play again

print("Thank you for playing!")
