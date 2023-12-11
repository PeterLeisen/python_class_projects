from cryptography.fernet import Fernet

from key_generator import Key_Generator
from key_loading import Key_Loading
from add_pwrd import Add_Pwrd
from view_pwrds import View_Pwrds


    # One Time Operation that Writes the Key
#Key_Generator.writing_key()

keey = Key_Loading.loading_key()
fern = Fernet(keey)

def view_pwrds():
    with open('pwords.txt', 'r') as f:
        for lines in f.readlines():
            inform = lines.rstrip()
            user_name, pword = inform.split("|")
            print("User:", user_name, "| Password:", fern.decrypt(pword.encode()).decode())

def pass_wrd_list():
    while True:
        mode = input("Please decide to either view your existing passwords or add a new password: (view, add), press q to quit? ").lower() 
        if mode == "q":
            break
        if mode == "view":
            view_pwrds()            
            #View_Pwrds.view_pwrds()
        elif mode == "add":
            Add_Pwrd.add_psswrd()       
        else: 
            print("Invalid entry.")
            continue
            