class Rational:
    # Constructor to initialize the numerator (p) and denominator (q) of the rational number
    def __init__(self, p, q) -> None:
        self.p = p  # Numerator
        self.q = q  # Denominator

    # Method to add two Rational objects using the formula (a/b + c/d = (ad + bc) / bd)
    def __add__(self, other):
        num = (
            self.p * other.q + self.q * other.p
        )  # Calculate the numerator of the result
        den = self.q * other.q  # Calculate the denominator of the result
        val = Rational(num, den)  # Create a new Rational object with the result
        return val  # Return the new Rational object

    # Method to represent the Rational object as a string in the form of 'p/q'
    def __str__(self) -> str:
        return str(self.p) + "/" + str(self.q)  # Return the string representation


# Create a Rational object representing 2/3
r1 = Rational(2, 3)
# Create another Rational object representing 1/2
r2 = Rational(1, 2)

# Print the second Rational object (1/2)
print(r2)
# Print the first Rational object (2/3)
print(r1)
# Add the two Rational objects and print the result
r3 = r1 + r2
print(r3)  # This will print the result of adding 2/3 and 1/2
