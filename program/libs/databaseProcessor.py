import sqlite3
import program.libs.mailer as mailer
import program.libs.activeKeyRandomizer as key
import time
import json


class AccountManager():

    def __init__(self, email=None, login=None, password=None):
        self.email = email
        self.login = login
        self.password = password
        
        self.list = []
        
        self.conn = sqlite3.connect(f'./program/database/clients.db')
        self.cur = self.conn.cursor()
        self.cur.execute(
            "create table if not exists credentials (role text, email text, login text, password text)"
            )
        
        for admin in self.cur.execute(
            "select login from credentials"):
            self.list.extend(admin)
        if 'admin' not in self.list:
            self.cur.execute(
            "insert into credentials values (?, ?, ?, ?)", 
            ('admin', 'yourEmail@gmail.com', 'admin', 'Z=u^9iN&5H')
            )
        if 'test' not in self.list:
            self.cur.execute(
            "insert into credentials values (?, ?, ?, ?)", 
            ('user', 'test@gmail.com', 'test', '')
            )
        self.conn.commit() # Z=u^9iN&5H     
        
    def createCredentials(self):
        self.cur.execute(
            f"insert into credentials values (?, ?, ?, ?)", 
            ('user', self.email, self.login, self.password)
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
        if self.checkClientData('login', self.login):
            return False
        
        activeKey = key.Randomizer()
        if mailer.Sender(self.email, activeKey.generateKay()).send():
            if activeKey.keyApprove(input('CODE: ')):
                self.createCredentials()
                self.closeDatabase()
                print('Client created successfully!')
                time.sleep(2)
                return True
        print('\nSomething went wrong!\nDid you provide the correct verification code?\n')
        time.sleep(5)
        return True
    
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
    
    def defineRank(self, user):
        for x in self.cur.execute("select role from credentials where login = ?",(user,)):
            return json.dumps(x)
        
    def deleteAccount(self):
        self.cur.execute("delete from credentials where login = ?",(self.login,))
        self.conn.commit()
    
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
                
    
    