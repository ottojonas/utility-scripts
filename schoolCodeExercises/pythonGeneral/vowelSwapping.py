def swapVowels(userString):
    vowels = "aeiou"
    vowelIndecies = [i for i, c in enumerate(userString) if c in vowels]
    stringList = list(userString)

    for i in range(len(vowelIndecies) // 2):
        j = vowelIndecies[i]
        k = vowelIndecies[-i - 1]
        stringList[j], stringList[k] = stringList[k], stringList[j]

    result = ""
    for char in stringList:
        result += char
    return result


userString = input("Enter a string: ")
print(swapVowels(userString))
