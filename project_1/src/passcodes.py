from cryptography.fernet import Fernet

# One Time Operation that Writes the Key
''' 
def writing_key():
    kee = Fernet.generate_key()
    with open("secret.key", "wb") as one_time_file:
        one_time_file.write(kee)

writing_key()  '''   #1:39:40 shows documentation, and description

def Loading_Key():
    return open(secret.tool)

def View_Pwrds():
    with open('pwords.txt', 'r') as f:
        for lines in f.readlines():
            inform = lines.rstrip()
            userName, pword = inform.split("|")
            print("User:", userName, "| Password:", pword)

def AddPwrd():
    AccountName = input('Account Name: ')
    PassWrd = input("Password: ")

    with open('pwords.txt', 'a') as f:
        f.write(AccountName + "|" + PassWrd + "\n")



def PassWrd_List():
    
    #pwd = input("Create a master password by typing here:  ")

    while True:
        mode = input("Please decide to either view your existing passwords or add a new password: (view, add), press q to quit? ").lower() 
        if mode == "q":
            break

        if mode == "view":
            View_Pwrds()
        elif mode == "add":
            AddPwrd()
        else: 
            print("Invalid entry.")
            continue
            

    #print("Testing")

    #Testing changes