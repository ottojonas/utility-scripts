def reverseString(string, index=0):
    if index == len(string):
        return ""
    else:
        return reverseString(string, index + 1) + string[index]


string = input("Enter a string to reverse: ")
result = reverseString(string, index=0)
print(result)
