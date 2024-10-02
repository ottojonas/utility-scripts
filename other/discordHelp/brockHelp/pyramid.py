def pattern(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        for x in range(i - 1, 0, -1):
            print(x, end=" ")
        print(" ")
    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        for x in range(i - 1, 0, -1):
            print(x, end=" ")
        print(" ")


userInput = int(input("Enter a number: "))
temp = pattern(userInput)
