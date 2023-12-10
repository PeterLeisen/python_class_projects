from cryptography.fernet import Fernet

from key_generator import Key_Generator

    # One Time Operation that Writes the Key
#Key_Generator.writing_key()

def loading_key():
    filee = open("secretss.key", "rb")
    keyy = filee.read()
    return keyy

keey = loading_key()
fern = Fernet(keey)

def view_pwrds():
    with open('pwords.txt', 'r') as f:
        for lines in f.readlines():
            inform = lines.rstrip()
            userName, pword = inform.split("|")
            print("User:", userName, "| Password:", fern.decrypt(pword.encode()).decode())

def add_pwrd():
    AccountName = input('Account Name: ')
    PassWrd = input("Password: ")

    with open('pwords.txt', 'a') as f:
        f.write(AccountName + "|" + fern.encrypt(PassWrd.encode()).decode() + "\n")

def PassWrd_List():

    while True:
        mode = input("Please decide to either view your existing passwords or add a new password: (view, add), press q to quit? ").lower() 
        if mode == "q":
            break

        if mode == "view":
            view_pwrds()

        elif mode == "add":
            add_pwrd()

        else: 
            print("Invalid entry.")
            continue
            
