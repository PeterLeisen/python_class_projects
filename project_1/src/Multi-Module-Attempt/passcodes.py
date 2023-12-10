from cryptography.fernet import Fernet

from Key_Maker import Key_Generator
#from Operations import ViewAdd

    # One Time Operation that Writes the Key
#Key_Generator.writing_key()

def Loading_Key():
    filee = open("secretss.key", "rb")
    keyy = filee.read()
    return keyy

keey = Loading_Key()
fern = Fernet(keey)

def View_Pwrds():
    with open('pwords.txt', 'r') as f:
        for lines in f.readlines():
            inform = lines.rstrip()
            userName, pword = inform.split("|")
            print("User:", userName, "| Password:", fern.decrypt(pword.encode()).decode())

def AddPwrd():
    AccountName = input('Account Name: ')
    PassWrd = input("Password: ")

    with open('pwords.txt', 'a') as f:
        f.write(AccountName + "|" + fern.encrypt(PassWrd.encode()).decode() + "\n")

def PassWrd_List():
    
    #pwd = input("Create a master password by typing here:  ")

    while True:
        mode = input("Please decide to either view your existing passwords or add a new password: (view, add), press q to quit? ").lower() 
        if mode == "q":
            break

        if mode == "view":
            View_Pwrds()
            #ViewAdd.View_Pwrds()
        elif mode == "add":
            AddPwrd()
            #ViewAdd.AddPwrd()
        else: 
            print("Invalid entry.")
            continue
            

    #print("Testing")

    #Testing changes