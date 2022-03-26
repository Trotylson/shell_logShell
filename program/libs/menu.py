import program.libs.loginManager as loginManager
import program.libs.databaseProcessor as processor
import program.logo as logo
import program.libs.devTools as console
import time


_author = 'Trotyl'
_version = '1.3.1'
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
    
        self._create = 'create account'
        self._edit = 'edit account'
        self._delete = 'delete account'
        self._logout = 'logout'
        self._admin = 'admin panel'
        _rank = processor.AccountManager().defineRank(user)

        while True:
            console.clear()
            logo.logo()
            
            choice = input(
                str(f'\n{service}\nver.{_version} by {_author}\n\nlogin as: {user} {_rank}\n\n'
                    f'\t1 - {self._create}\n'
                    f'\t2 - {self._delete}\n'
                    f'\t3 - {self._admin}\n'
                    f'\tx - {self._logout}\n'
                    f'\nchoice: ').lower()
                )
            if choice == '1' or choice == '2' or choice == '3' or choice == 'x':
                if choice == '1':
                    while True:
                        flag = processor.AccountManager(
                            email = manager.getEmail(), login = manager.getLoginName(), password = manager.getPassword()
                            ).processNewClient()
                        if flag:
                            break
                elif choice == '2':
                    if panel.deleteAccount():
                        processor.AccountManager(login=user).deleteAccount()
                        print('Account deleted...')
                        time.sleep(2)
                        break
                    print('Account still in use')
                    time.sleep(2)
                elif choice == '3':
                    if _rank == 'admin': AdminPanel()
                    else: 
                        print(f'User rang: {user}:{_rank} - permissions too low!')
                        time.sleep(2)
                elif choice == 'x':
                    break
            else:    
                print('Wrong choice, please try again!')
                
class AdminPanel():
    
    def __init__(self):
        print('Admin panel')
        time.sleep(2)