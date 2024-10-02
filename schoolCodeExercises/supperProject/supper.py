import csv

with open("supperProject/suppermarket.csv", "r") as supperFile:
    csvReader = csv.reader(supperFile)
    supperArray = list(csvReader)


def printReceipt():
    total = 0
    decoratingTotal = 0
    gardeningTotal = 0
    for row in supperArray:
        item, category, price = row[0], row[1], float(row[2])
        originalPrice = price
        if category == "Decorating":
            decoratingTotal += price
            total += price
            print(f"{item}: {price}")
        elif category == "Gardening":
            gardeningTotal += price
            total += price
            discount = 0
            if decoratingTotal >= 20:
                discount = price * 0.1
                price -= discount
                gardeningTotal -= discount
                total -= discount
            print(f"{item}: {originalPrice}")
            if discount > 0:
                print(f"-£{discount:.2f} discount")
    print(f"Total: {total:.2f}")


printReceipt()
