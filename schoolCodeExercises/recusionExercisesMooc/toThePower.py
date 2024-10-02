def toThePower(base, exp):
    if exp == 0:
        return 1
    else:
        return base * toThePower(base, exp - 1)


base = int(input("Enter the base number: "))
exp = int(input("Enter the exp number: "))
result = toThePower(base, exp)
print(result)
