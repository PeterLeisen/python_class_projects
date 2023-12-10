class key_loading:
    
    def Loading_Key():
        filee = open("secretss.key", "rb")
        keyy = filee.read()
        return keyy