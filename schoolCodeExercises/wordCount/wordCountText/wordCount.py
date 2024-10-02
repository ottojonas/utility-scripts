from icecream import ic


def addToDict(word, wordCountDictionary):
    if word in wordCountDictionary:
        wordCountDictionary[word] += 1
    else:
        wordCountDictionary[word] = 1


def mostCommon(wordCountDictionary, numberOfWords):
    wordCountItems = [(word, count) for word, count in wordCountDictionary.items()]
    for i in range(len(wordCountItems)):
        for j in range(len(wordCountItems) - i - 1):
            if wordCountItems[j][1] < wordCountItems[j + 1][1]:
                wordCountItems[j], wordCountItems[j + 1] = (
                    wordCountItems[j + 1],
                    wordCountItems[1],
                )
    return wordCountItems[:numberOfWords]


def isPunctuationCharacter(character):
    return character in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


def removePunctuationFromLine(line):
    return "".join(
        character for character in line if not isPunctuationCharacter(character)
    )


files = [
    "wordCount/wordCountText/swift.txt",
    "wordCount/wordCountText/dickens.txt",
    "wordCount/wordCountText/orwell.txt",
    "wordCount/wordCountText/rowling.txt",
]

longWords = []

for file in files:
    bookWordCount20 = {}
    bookWordCount = {}
    totalBookWords = 0

    with open(file, "r") as bookFile:
        for line in bookFile.read().split("\n"):
            line = removePunctuationFromLine(line)
            words = line.split()
            totalBookWords += len(words)
            for word in words:
                addToDict(word, bookWordCount)
                addToDict(word, bookWordCount20)

    mostCommon20 = mostCommon(bookWordCount20, 20)
    ic(f"20 Most Common Words In {file}: {mostCommon20}")
    ic(f"Word Count For {file}: {bookWordCount}")
    ic(f"Total words in {file}: {totalBookWords}")

    with open("wordCount/wordCountText/words.txt") as wordsFile:
        wordsList = wordsFile.read().split("\n")
        notInBook = [word for word in wordsList if word not in bookWordCount]
        longWords = [word for word in wordsList if len(word) > 20]
        ic(f"Words not in book {file}: {notInBook}")
        ic(f"Number of words not in book {file}: {len(notInBook)}")
ic(f"Words with more than 20 characters: {longWords}")
ic(f"Number of words with more than 20 characters: {len(longWords)}")
