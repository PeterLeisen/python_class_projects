
class ViewAdd:


    '''
    def Loading_Key():
        filee = open("secretss.key", "rb")
        keyy = filee.read()
        return keyy'''
'''
keey = Loading_Key()
fern = Fernet(keey)'''


    def View_Pwrds():
        from cryptography.fernet import Fernet
        from Key_Loading import key_loading

        keey = key_loading.Loading_Key()
        fern = Fernet(keey)
        
        with open('pwords.txt', 'r') as f:
            for lines in f.readlines():
                inform = lines.rstrip()
                userName, pword = inform.split("|")
            print("User:", userName, "| Password:", fern.decrypt(pword.encode()).decode())

    def AddPwrd():
        from cryptography.fernet import Fernet
        from Key_Loading import key_loading

        keey = key_loading.Loading_Key()
        fern = Fernet(keey)

        AccountName = input('Account Name: ')
        PassWrd = input("Password: ")

        with open('pwords.txt', 'a') as f:
            f.write(AccountName + "|" + fern.encrypt(PassWrd.encode()).decode() + "\n")