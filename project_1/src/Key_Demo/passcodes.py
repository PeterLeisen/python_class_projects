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
    account_name = input('Account Name: ')
    pass_wrd = input("Password: ")

    with open('pwords.txt', 'a') as f:
        f.write(account_name + "|" + fern.encrypt(pass_wrd.encode()).decode() + "\n")

def pass_wrd_list():

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
            
