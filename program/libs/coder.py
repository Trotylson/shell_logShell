

CodeDictionary = {'a':'Z=','ą':'!y','b':'X?','c':'w0','ć':'1V','d':'u^','e':'$T','ę':'s0',
                  'f':'@Q','g':'p?','h':'@o','i':'N&','j':'mX','k':'!L','l':'k@','ł':'$J',
                  'm':'9i','n':'5H','ń':'g%','o':'3F','ó':'4f','p':'E$','q':'0c','r':'B>',
                  's':'!a','ś':'5+','t':'82','u':'0F','v':'-x','w':'vV','x':'+!','y':'\!',
                  'z':'B5','ż':'5b','ź':'6b',
                  ' ':'&i','.':'\e',',':'\i',':':'\d'}

class Crypto():
    
    def __init__(self, password):
        self.password = password
        self.crypto = ''
    
    def encode(self):
        for x in self.password:
            self.crypto += CodeDictionary[x]
        return self.crypto
    
    def decode(self):
        coded = ""
        for x in self.password:
            coded += x
            if coded in CodeDictionary.values():
                self.crypto += list(CodeDictionary.keys())[list(CodeDictionary.values()).index(coded)]
                coded = ""
        return self.crypto
        
    