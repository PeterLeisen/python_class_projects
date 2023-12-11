class Key_Loading:
    
    def loading_key():
        filee = open("secretss.key", "rb")
        keyy = filee.read()
        return keyy
