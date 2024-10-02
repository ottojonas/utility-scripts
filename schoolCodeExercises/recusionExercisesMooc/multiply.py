def recursiveMultiply(num1, num2):
    if num2 <= 1:
        return num1 * num2
    else:
        return num1 + recursiveMultiply(num1, num2 - 1)


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = recursiveMultiply(num1, num2)
print(result)
