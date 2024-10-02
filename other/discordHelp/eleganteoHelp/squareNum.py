# Define the main function
def main():
    # Prompt the user for input, convert it to an integer, and assign it to x
    x = int(input("What's x? "))
    # Print the result of squaring x by calling the square function
    print("x squared is", square(x))


# Define the square function that takes a single argument n
def square(n):
    # Return the square of n
    return n**2


# Call the main function to start the program
main()
