

class Manager():
    
    def getLoginName(self):
        login_name = input('Select your login: ')
        return login_name
    
    def getEmail(self):
        email = input('Enter your email address: ')
        return email
    
    def getRetypePassword(self, password):
        retype = input('Retypy your password: ')
        if password != retype:
            print('Password mismatch!')
            return True
        return False
    
    def getPassword(self):
        while True:
            password = input('Select your password: ')
            if self.getRetypePassword(password):
                pass # print('Password mismatch!')
            else: return password
            
    
    
    