hashTable = []


def getDomain(url):
    start = url.find("//") + 2
    end = url.find("/") + 2
    if end == -1:
        end = len(url)
    return url[start:end]


def hashDomain(domain):
    domain = domain.upper()
    return sum(ord(char) for char in domain)


def addToHashTable(hashedDomain):
    hashTable.append(hashedDomain)


def main():
    url = input("Enter a web address to hash: ")
    domain = getDomain(url)
    hashedDomain = hashDomain(domain)
    addToHashTable(hashedDomain)
    print("Hashed domain added to the hash table")
    print(hashTable)


if __name__ == "__main__":
    main()
