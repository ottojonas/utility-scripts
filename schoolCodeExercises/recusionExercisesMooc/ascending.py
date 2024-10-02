def ascending(n, start=0):
    if start > n:
        return
    print(start)
    ascending(n, start + 1)


n = int(input("Enter a number: "))
result = ascending(n, start=0)
print(result)
