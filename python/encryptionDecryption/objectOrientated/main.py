from icecream import ic 

class Encrypt: 
    def __init__(self): 
        self.send = ""
        self.res = []

    def sender(self): 
        self.send = input("enter the data to encrypt: ")
        self.res = [ord(i) + 2 for i in self.send]
        ic(f"encrypted data: {"".join(chr(i) for i in self.res}")

class Decrypt: 
    def receiver(self): 
    decryptedData = "".join(chr(i-2) for i in self.res)
    ic(f"decrypted data: {decryptedData}")
object = Decrypt() 
object.sender() 
ob.receiver()
