import sqlite3

class Creator():

    def __init__(self, email, login_name, password):
        self.email = email
        self.login_name = login_name
        self.password = password
        
        self.conn = sqlite3.connect(f'./program/database/clients.db')
        self.cur = self.conn.cursor()
        self.cur.execute("create table if not exists credentials (email text, login text, password text)")
        
    def createCredentials(self):
        self.cur.execute(f"insert into credentials values (?, ?, ?)", (self.email, self.login_name, self.password))
        self.conn.commit()
        
    def checkClientEmail(self):
        for data in self.cur.execute("select email from credentials"):
            if self.email in data:
                print(f'{data} email already exists!')
                return True
        return False
    
    def checkClientLogin(self):
        for data in self.cur.execute("select login from credentials"):
            if self.login_name in data:
                print(f'{data} login already exists!')
                return True
        return False
    
    def closeDatabase(self):
        self.conn.close()
                
    
        