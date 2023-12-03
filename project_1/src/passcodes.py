


def view():
    pass

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")



def passcode_list():
    
    #pwd = input("Create a master password by typing here:  ")

    mode = input("Please choose weither to view existing passwords or add a new password: (view, add), press q to quit? ").lower() 

    while True:
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