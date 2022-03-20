import program.libs.loginManager as loginManager
import program.libs.databaseProcessor as processor
import program.logo as logo
import program.libs.devTools as console
import time


_author = 'Trotyl'
_version = '1.3'
service = 'LogShell'

manager = loginManager.CreatorManager()
panel = loginManager.LogginPanel()

user = ''

class Menu():
    
    def __init__(self):
        
        self.poz_one = 'login'
        self.poz_two = 'exit'
        
        while True:
            console.clear()
            logo.logo()
            choice = input(
                str(f'\n{service}\nver.{_version} by {_author}\n\n\t1 - {self.poz_one}\n\t2 - {self.poz_two}\n\nchoice: ')
                )
            if choice == '1' or choice == '2':
                if choice == '1':
                    while True:
                        global user
                        user = panel.getLogin()
                        flag = processor.AccountManager(login = user, password = panel.getPassword()).processLogin()
                        if flag:
                            ShellMenu()
                            break
                elif choice =='2':
                    processor.AccountManager(self).closeDatabase()
                    print('Bye! :)')
                    exit()
            else:    
                print('Wrong choice, please try again!')

class ShellMenu():
    
    def __init__(self):
    
        self.poz_one = 'create account'
        self.poz_two = 'delete account'
        self.poz_three = 'logout'
        _rank = processor.AccountManager().defineRank(user)

        while True:
            console.clear()
            logo.logo()
            choice = input(
                str(f'\n{service}\nver.{_version} by {_author}\n\nlogin as: {user} {_rank}\n\n\t1 - {self.poz_one}\n\t2 - {self.poz_two}\n\t3 - {self.poz_three}\n\nchoice: ')
                )
            if choice == '1' or choice == '2' or choice == '3':
                if choice == '1':
                    while True:
                        flag = processor.AccountManager(
                            email = manager.getEmail(), 
                            login = manager.getLoginName(), 
                            password = manager.getPassword()
                            ).processNewClient()
                        if flag:
                            break
                if choice == '2':
                    if panel.deleteAccount():
                        processor.AccountManager(login=user).deleteAccount()
                        print('Account deleted...')
                        time.sleep(2)
                        break
                    print('Account still in use')
                    time.sleep(2)
                if choice == '3':
                    break