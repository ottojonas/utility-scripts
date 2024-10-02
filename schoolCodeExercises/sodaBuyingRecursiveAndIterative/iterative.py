def bottleRecycle(money, emptyBottles=0):
    totalBottles = 0
    while money > 0 or emptyBottles >= 3:
        if money > 0:
            money -= 1
            emptyBottles += 1
            totalBottles += 1
        elif emptyBottles >= 3:
            emptyBottles -= 2
            totalBottles += 1
    return totalBottles


money = int(input("Enter the amount of money you have to spend: £"))
result = bottleRecycle(money, emptyBottles=0)
print(result)
