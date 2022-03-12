import program.libs.creatorManager as creatorManager
import program.libs.loginManager as loginManager
import program.libs.processor as processor
import program.accessArea.access as access


_author = 'Trotyl'
_version = 0.1

cMan = creatorManager.Manager()
lMan = loginManager.LoginPanel()

service = 'loginService'
poz_one = 'create account'
poz_two = 'login'
poz_three = 'exit'





while True:
    choice = input(
        str(f'\n{service} v{_version}\nby {_author}\n\n\t1 - {poz_one}\n\t2 - {poz_two}\n\t3 - {poz_three}\n\nchoice: ')
        )
    if choice == '1' or choice == '2' or choice == '3':
        if choice == '1':
            while True:
                flag = processor.Processor.processNewClient(cMan.getEmail(), cMan.getLoginName(), cMan.getPassword())
                if flag:
                    break
            
        elif choice =='2':
            while True:
                flag = processor.Processor.processLogin(lMan.getLogin(), lMan.getPassword())
                if flag:
                    access.access()
                    break
        elif choice =='3':
            print('Bye! :)')
            exit()
        else:    
            print('Wrong choice, please try again!')
    
exit()