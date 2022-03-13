import getpass

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
            else: return password


class LogginPanel():
    
    def getLogin(self):
        login = input('login: ')
        return login
    
    def getPassword(self):
        password = getpass.getpass('password: ')    # input('password: ')
        return password