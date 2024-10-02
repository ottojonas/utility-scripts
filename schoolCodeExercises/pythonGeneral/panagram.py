import string


def isPanagram(sentence):
    alphabet = set(string.ascii_lowercase)
    return set(sentence.lower()) >= alphabet


sentence = input("Enter a sentence to check: ")

if isPanagram(sentence):
    print("The sentence is a panagram")
else:
    print("The sentence is not a panagram")
