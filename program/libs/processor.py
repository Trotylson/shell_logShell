import program.libs.databaseManager as dbManager

class Processor():
    
    

    def processLogin(login, password):
        _log = False
        _pass = False
        credentials = dbManager.Logger(login, password)
        if credentials.checkClientLogin():
            # print('login correct!')
            _log = True
        else: print('login incorrect!')    
        if credentials.checkClientPassword():
            # print('password correct!')
            _pass = True
        else: print('password incorrect!')
        if _log and _pass:
            credentials.closeDatabase()
            print('Credentials correct!')
            return True
        credentials.closeDatabase()
        print('FAIL LOGGING')
        return False