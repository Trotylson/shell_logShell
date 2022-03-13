import sqlite3

class Creator():

    def __init__(self, email, login_name, password):
        self.email = email
        self.login_name = login_name
        self.password = password
        
        self.conn = sqlite3.connect(f'./program/database/clients.db')
        self.cur = self.conn.cursor()
        self.cur.execute(
            "create table if not exists credentials (email text, login text, password text)"
            )
        
    def createCredentials(self):
        self.cur.execute(
            f"insert into credentials values (?, ?, ?)", 
            (self.email, self.login_name, self.password)
            )
        self.conn.commit()
        
    def checkClientData(self, column, value):
        for data in self.cur.execute(f"select {column} from credentials"):
            if value in data:
                print(f'{data} {column} already exists!')
                return True
        return False
    
    def closeDatabase(self):
        self.conn.close()
    
    def processNewClient(self):
        if self.checkClientData('email', self.email):
            return False
        if self.checkClientData('login', self.login_name):
            return False
        # if password == False:
        #     return True
        self.createCredentials()
        self.closeDatabase()
        print('Client created successfully!')
        return True
                
    
class Logger():
    
    def __init__(self, login, password):
        self.login = login
        self.password = password
        
        self.conn = sqlite3.connect(
            f'./program/database/clients.db'
            )
        self.cur = self.conn.cursor()
        
    def checkClientLogin(self):
        for data in self.cur.execute(
            "select login from credentials"):
            if self.login in data:
                # print(f'{data} login correct!')
                return True
        # print(f'login incorrect!')
        return False
    
    def checkClientPassword(self):
        for data in self.cur.execute(
            "select password from credentials where login = ?", 
            (self.login,)):
            if self.password in data:
                # print(f'{data} login correct!')
                return True
        # print(f'password incorrect!')
        return False
    
    def closeDatabase(self):
        self.conn.close()
        
    def processLogin(self):
        _log = False
        _pass = False
        if self.checkClientLogin():
            # print('login correct!')
            _log = True
        else: print('login incorrect!')    
        if self.checkClientPassword():
            # print('password correct!')
            _pass = True
        else: print('password incorrect!')
        if _log and _pass:
            self.closeDatabase()
            print('Credentials correct!')
            return True
        self.closeDatabase()
        print('FAIL LOGGING')
        return False
    
    
class AccountManager():
    pass