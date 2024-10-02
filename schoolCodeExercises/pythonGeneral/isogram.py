def isIsogram(word):
    word = word.lower()
    return len(word) == len(set(word))


word = input("Enter a word to check: ")

if isIsogram(word):
    print(f"{word} is an isogram")
else:
    print(f"{word} is not an isogram")
