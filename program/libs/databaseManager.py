import sqlite3

conn = sqlite3.connect(f'./program/database/clients.db')
cur = conn.cursor()
cur.execute("create table if not exists credentials (email text, login text, password text)")

class Creator():
    
    def __init__(self, email, login_name, password):
        self.email = email
        self.login_name = login_name
        self.password = password
        
    def createCredentials(self):
        cur.execute(f"insert into credentials values (?, ?, ?)", (self.email, self.login_name, self.password))
        conn.commit()
        
    def checkClient(self):
        for data in cur.execute("select * from credentials"):
            print(data)
                

class Persistance(Creator):
        
    def checkClient(email, login, password):
        for data in cur.execute("select * from credentials"):
            print(data)
    

# conn.close()
        