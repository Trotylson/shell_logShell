import program.libs.loginManager as loginManager
import program.libs.loginProcessor as processor
import program.logo as logo
import program.libs.devTools as console

_author = 'Trotyl'
_version = '1.2.1'

service = 'LogShell'
poz_one = 'create account'
poz_two = 'login'
poz_three = 'exit'

manager = loginManager.CreatorManager()
panel = loginManager.LogginPanel()


while True:
    console.clear()
    logo.logo()
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
                flag = processor.Loger(panel.getLogin(), panel.getPassword()).processLogin()
                if flag:
                    # inside menu
                    break
        elif choice =='3':
            print('Bye! :)')
            exit()
    else:    
        print('Wrong choice, please try again!')
    
