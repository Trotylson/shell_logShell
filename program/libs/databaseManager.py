import sqlite3

class Creator():
    
    def __init__(self, login_name, password, email):
        self.email = email
        self.login_name = login_name
        self.password = password
        
        self.conn = sqlite3.connect(f'./program/database/{self.login_name}.db')
        self.cur = self.conn.cursor()
        
        self.cur.execute("create table if not exists client values (email text, login text, password text)")
        
    def createCredentials(self):
        self.cur.execute(f"insert into {self.login_name} values (?, ?, ?)", (self.email, self.login_name, self.password))
        

class Persistance():
    
    def __init__(self, email, login_name, password):
        self.email = email
        self.login_name = login_name
        self.password = password
        
    def checkClient(self):
        try:
            self.conn = sqlite3.connect(f'./program/database/{self.login_name}.db')
            self.cur = self.conn.cursor()
            self.conn.close()
            return False
        except Exception:
            return True
    
        
    
    
        