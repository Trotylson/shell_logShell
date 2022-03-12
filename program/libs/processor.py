import program.libs.databaseManager as dbManager

class Processor():
    
    def checkLogin():
        pass
    
    def processNewClient(email, login, password):
        client = dbManager.Creator(email, login, password)
        if client.checkClient():
            return True
        client.createCredentials()
        
        print('Client created successfully!')


# dbManager.conn.close()