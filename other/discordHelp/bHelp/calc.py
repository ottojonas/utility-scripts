# float input storing the input as "num1" and "num2"
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


print("Choose an operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# integer input storing value as "choice" allowing the user to select what action they want
choice = int(input("Enter choice(1/2/3/4): "))

# if and elif loop
# elif means "else if"
if choice == 1:
    result = num1 + num2
    print("The result of addition is: " + str(result))
elif choice == 2:
    result = num1 - num2
    print("The result of subtraction is: " + str(result))
elif choice == 3:
    result = num1 * num2
    print("The result of multiplication is: " + str(result))
elif choice == 4:
    result = num1 / num2
    print("The result of division is: " + str(result))
