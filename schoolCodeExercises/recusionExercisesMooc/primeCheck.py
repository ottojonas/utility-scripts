def primeCheck(number, i=2):
    if number < 2:
        return False
    elif i == number:
        return True
    elif number % i == 0:
        return False
    else:
        return primeCheck(number, i + 1)


number = int(input("Enter a number to check: "))
result = primeCheck(number, i=2)
print(result)
