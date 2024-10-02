# test_calculator.py

# Import the square function from the calculator module
from calculator import square


# Define a test function to validate the square function
def testSquare():
    # Test if the square of 2 is correctly calculated as 4
    if square(2) != 4:
        # Print an error message if the square of 2 is not 4
        print("2 squared was not 4")
    # Test if the square of 3 is correctly calculated as 9
    elif square(3) != 9:
        # Print an error message if the square of 3 is not 9
        print("3 squared was not 9")


testSquare()
