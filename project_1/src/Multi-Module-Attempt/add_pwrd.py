
class Add_Pwrd:


    def add_psswrd():
        from cryptography.fernet import Fernet
        from key_loading import Key_Loading

        keey = Key_Loading.loading_key()
        fern = Fernet(keey)
        account_name = input('Account Name: ')
        pass_wrd = input("Password: ")

        with open('pwords.txt', 'a') as f:
            f.write(account_name + "|" + fern.encrypt(pass_wrd.encode()).decode() + "\n")