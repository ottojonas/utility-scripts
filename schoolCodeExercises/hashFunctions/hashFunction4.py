def hash(siteName):
    firstDot = siteName.find(".")
    if firstDot != -1:
        siteName = siteName[firstDot + 1 :]
    secondDot = siteName.find(".")
    if secondDot != -1:
        siteName = siteName[:secondDot]
    siteName = siteName.upper()
    hashedValue = 0
    for char in range(len(siteName)):
        hashedValue = hashedValue + ord(siteName[char])
    return hashedValue


siteName = input("Enter a site name to hash: ")
hashingFunction = hash(siteName)
print(hashingFunction)
