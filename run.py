import program.libs.creatorManager as creatorManager
import program.libs.processor as processor


_author = 'Trotyl'
_version = 0.1

cMan = creatorManager.Manager()

service = 'loginService'
poz_one = 'create account'
poz_two = 'login'
poz_three = 'exit'


while True:
    flag = processor.Processor.processNewClient(
        cMan.getEmail(),
        cMan.getLoginName(),
        cMan.getRetypePassword(cMan.getPassword())
        )
    if flag == False:
        break


# while True:
#     choice = input(
#         str(f'\n{service}\n\n\t1 - {poz_one}\n\t2 - {poz_two}\n\t3 - {poz_three}\n\nchoice: ')
#         )
#     if choice == '1' or choice == '2' or choice == '3':
#         if choice == '1':
#             while True:
#                 flag = consider.processNewClient(
#                     cMan.getEmail() ,
#                     cMan.getLoginName(), 
#                     cMan.getRetypePassword(cMan.getPassword())
#                     )
#                 if flag == False:
#                     break
            
#         elif choice =='2':
#             print('Loging')
#             break
#         elif choice =='3':
#             print('Bye! :)')
#             exit()
#         else:    
#             print('Wrong choice, please try again!')
    
exit()