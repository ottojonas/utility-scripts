# Define a function to print a square of '#' characters
def printSquare(size):
    # Iterate over the range of size to print each row of the square
    for index in range(size):
        # Call the printRow function to print a single row of the square
        printRow(size)


# Define a function to print a single row of '#' characters
def printRow(width):
    # Print a row of '#' characters, where the number of '#' is equal to the width
    print("#" * width)


# Define the main function that serves as the entry point of the program
def main():
    # Call the printSquare function with a size of 10 to print a 10x10 square
    printSquare(10)


# Call the main function to run the program
main()
