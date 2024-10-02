def isEven(n):
    return True if n % 2 == 0 else False


def main():
    x = int(input("What is x? "))
    if isEven(x):
        print("Even")
    else:
        print("Odd")


main()
