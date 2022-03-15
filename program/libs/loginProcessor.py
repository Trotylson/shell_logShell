import sqlite3
import program.libs.mailer as mailer
import program.libs.activeKeyRandomizer as key


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
        
        activeKey = key.Randomizer()
        mailer.Sender(self.email, activeKey.generateKay()).send()
        if activeKey.keyApprove(input('CODE: ')):
            self.createCredentials()
            self.closeDatabase()
            print('Client created successfully!')
            return True
        print('\nSomething went wrong!\nDid you provide the correct verification code?\n')
        return False
                
    
class Loger():
    
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.list = []
        
        self.conn = sqlite3.connect(
            f'./program/database/clients.db'
            )
        self.cur = self.conn.cursor()
        
        self.cur.execute(
            "create table if not exists credentials (email text, login text, password text)"
            )
             
        for admin in self.cur.execute(
            "select login from credentials"):
            self.list.extend(admin)
        if 'admin' not in self.list:
            self.cur.execute(
            "insert into credentials values (?, ?, ?)", 
            ('yourEmail@gmail.com', 'admin', 'Z=u^9iN&5H')
            )
        self.conn.commit() # Z=u^9iN&5H
        
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
        else: 
            print('login incorrect!')
            return False
        if self.checkClientPassword():
            # print('password correct!')
            _pass = True
        else: 
            print('password incorrect!')
        if _log and _pass:
            self.closeDatabase()
            print('Credentials correct!')
            return True
        self.closeDatabase()
        print('FAIL LOGGING')
        return False
    
    
class AccountManager():
    pass