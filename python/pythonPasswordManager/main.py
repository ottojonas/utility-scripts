from cryptography.fernet import Fernet

"""def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_files:
        key_files.write(key)

"""


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())


def add():
    name = input("account name: ")
    password = input("account password: ")

    with open("passwords.txt", "a") as password_file:
        password_file.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")


while True:
    mode = input(
        "would you like to add a new password or view existing ones (view, add)? press q to quit: "
    ).lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode")
        break
