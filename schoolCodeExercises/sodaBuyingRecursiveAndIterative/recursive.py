def bottleRecycle(money, emptyBottles=0):
    if money < 0:
        return 0
    if money == 0 and emptyBottles < 3:
        return 0
    if emptyBottles >= 3:
        return 1 + bottleRecycle(money, emptyBottles - 3 + 1)
    return 1 + bottleRecycle(money - 1, emptyBottles + 1)


money = int(input("Enter the amount of money you have to spend: £"))
result = bottleRecycle(money, emptyBottles=0)
print(result)
