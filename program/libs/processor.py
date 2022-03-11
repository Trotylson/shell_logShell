import program.libs.databaseManager as dbManager

# creator = dbManager.Creator()

class Processor:
    
    def processNewClient(self, email, login, password):
        if dbManager.Persistance.checkClient(login):
           return True
        return False


# creator.conn.close()