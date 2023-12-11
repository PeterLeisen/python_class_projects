from cryptography.fernet import Fernet

class Key_Generator:

    
    def writing_key():
        kee = Fernet.generate_key()
        with open("secretss.key", "wb") as one_time_file:
            one_time_file.write(kee)

