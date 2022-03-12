import dbm
import program.libs.databaseManager as dbManager

class Processor():
    
    def processNewClient(email, login, password):
        client = dbManager.Creator(email, login, password)
        if client.checkClientEmail():
            return False
        if client.checkClientLogin():
            return False
        # if password == False:
        #     return True
        client.createCredentials()
        client.closeDatabase()
        print('Client created successfully!')
        return True


# dbManager.conn.close()