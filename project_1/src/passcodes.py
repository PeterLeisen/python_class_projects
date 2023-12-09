from cryptography.fernet import Fernet

'''
def writing_key():
    kee = Fernet.generate_key()
    with open("secret.tool", "wb") as one_time_file:
        one_time_file.write(kee)

writing_key()'''      #1:39:40 shows documentation, and description

def view():
    with open('passwords.txt', 'r') as f:
        for lines in f.readlines():
            data = lines.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", passw)

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")



def passcode_list():
    
    #pwd = input("Create a master password by typing here:  ")

    while True:
        mode = input("Please choose weither to view existing passwords or add a new password: (view, add), press q to quit? ").lower() 
        if mode == "q":
            break

        if mode == "view":
            view()
        elif mode == "add":
            add()
        else: 
            print("Invalid mode.")
            continue
            

    #print("Testing")

    #Testing changes