

class Manager():
    
    def getLoginName(self):
        login_name = input('Select your login: ')
        return login_name
    
    def getEmail(self):
        email = input('Enter your email address: ')
        return email
    
    def getPassword(self):
        password = input('Select your password: ')
        return password
    
    def getRetypePassword(self, password):
        retype = input('Retypy your password: ')
        if password != retype:
            print('Password mismatch!')
            return False
        return password
    