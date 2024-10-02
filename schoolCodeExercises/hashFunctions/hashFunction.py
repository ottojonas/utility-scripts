# Create lsit of n size
# Populte with None
# Repeat
#   Get web address
#   Extract domain name
#   Capitalise and create hash value
#   Add site to list

import hashlib
from urllib.parse import urlparse


def getDomain(url):
    return urlparse(url).netloc


def hashDomain(domain):
    domain = domain.upper()
    return hashlib.sha256(domain.encode()).hexdigest()


hashTable = []


def addToHashTable(hashedDomain):
    hashTable.append(hashedDomain)


def main():
    url = input("Enter a web address to hash: ")
    domain = getDomain(url)
    hashedDomain = hashDomain(domain)
    addToHashTable(hashedDomain)
    print("Hashed domain added to hash table")
    print(hashTable)


if __name__ == "__main__":
    main()
