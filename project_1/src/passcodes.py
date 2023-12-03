


def passcode_list():
    
    #pwd = input("Create a master password by typing here:  ")

    mode = input("Please choose weither to view existing passwords or add a new password: (view, add), press q to quit? ").lower() 

    while True:
        if mode == "q":
            break
        if mode == "view":
            pass
        elif mode == "add":
            pass
        else: 
            print("Invalid mode.")
            continue

    #print("Testing")

    #Testing changes