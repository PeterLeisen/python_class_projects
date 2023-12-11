
class View_Pwrds:

    def view_pwrds():
        from cryptography.fernet import Fernet
        from key_loading import Key_Loading

        keey = Key_Loading.loading_key()
        fern = Fernet(keey)
        
        with open('pwords.txt', 'r') as f:
            for lines in f.readlines():
                inform = lines.rstrip()
                user_name, pword = inform.split("|")
            print("User:", user_name, "| Password:", fern.decrypt(pword.encode()).decode())

