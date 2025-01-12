data = [['A1', 28], ['A2', 32], ['A3', 1], ['A4', 0],
        ['A5', 10], ['A6', 22], ['A7', 30], ['A8', 19],
	['B1', 145], ['B2', 27], ['B3', 36], ['B4', 25],
	['B5', 9], ['B6', 38], ['B7', 21], ['B8', 12],
	['C1', 122], ['C2', 87], ['C3', 36], ['C4', 3],
	['D1', 0], ['D2', 5], ['D3', 55], ['D4', 62],
	['D5', 98], ['D6', 32]]

sitesNumber = len(data)
print("There are", sitesNumber, "sites")
print(data[6][1], "Birds were counted in the 7th site") 
print(data[25][1], "Birds were counted in the last site")
#Total number of birds
total = 0 
for i in range(len(data)):
    total = total + data[i][1]
print(total, "Birds in total") 
#average number of birds
average = total / sitesNumber
print("There were an average of", average, "birds per site")

#number of birds with a "C" label
cTotal = 0 
for i in range(len(data)): 
    if "C" in data[i][0]:
        cTotal = cTotal + data[i][1]
print("There are", cTotal, "birds in the C sites") 