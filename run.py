import program.libs.logginManager as logginManager
import program.libs.logginProcessor as processor
import program.logo as logo

_author = 'Trotyl'
_version = 1.0

service = 'loggingSystem'
poz_one = 'create account'
poz_two = 'login'
poz_three = 'exit'

manager = logginManager.CreatorManager()
panel = logginManager.LogginPanel()

logo.access()

while True:
    choice = input(
        str(f'\n{service}\nver.{_version} by {_author}\n\n\t1 - {poz_one}\n\t2 - {poz_two}\n\t3 - {poz_three}\n\nchoice: ')
        )
    if choice == '1' or choice == '2' or choice == '3':
        if choice == '1':
            while True:
                flag = processor.Creator(manager.getEmail(), manager.getLoginName(), manager.getPassword()).processNewClient()
                if flag:
                    break
            
        elif choice =='2':
            while True:
                flag = processor.Logger(panel.getLogin(), panel.getPassword()).processLogin()
                if flag:
                    logo.access()
                    break
        elif choice =='3':
            print('Bye! :)')
            exit()
    else:    
        print('Wrong choice, please try again!')
    
