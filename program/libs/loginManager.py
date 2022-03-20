import getpass
import program.libs.coder as coder

class CreatorManager():
    
    def getLoginName(self):
        login_name = input('Select your login: ')
        return login_name
    
    def getEmail(self):
        email = input('Enter your email address: ')
        return email
    
    def getRetypePassword(self, password):
        retype = getpass.getpass('Retype password: ')# input('Retypy your password: ')
        if password != retype:
            print('Password mismatch!')
            return True
        return False
    
    def getPassword(self):
        while True:
            password = getpass.getpass('Select password: ') # input('Select your password: ')
            if self.getRetypePassword(password):
                pass # print('Password mismatch!')
            else: return coder.Crypto(password).encode()


class LogginPanel():
    
    def getLogin(self):
        login = input('login: ')
        return login
    
    def getPassword(self):
        password = getpass.getpass('password: ')    # input('password: ')
        return coder.Crypto(password).encode()
    
    def deleteAccount(self):
        ask = input('Do you want to delete this account? [y / n]: ').lower()
        if ask == 'yes' or ask == 'y':
            return True
        return False