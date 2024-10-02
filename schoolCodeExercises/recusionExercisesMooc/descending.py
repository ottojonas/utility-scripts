def descending(n):
    if n < 0:
        return
    print(n)
    descending(n - 1)


n = int(input("enter the number: "))
result = descending(n)
print(result)
