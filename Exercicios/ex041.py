from datetime import date
from time import sleep
print('-=-=-=-=-=-= SISTEMA DA CNN -=-=-=-=-=-=')
anoNas = int(input('Em que ano você nasceu? '))
print('-=' * 20)
idade = date.today().year - anoNas
print('CALCULANDO...')
print('-=' * 20)
sleep(1.5)
if idade < 9:
    print(f'o atleta tem {idade} anos.')
    print('Você é nadador \033[32mMIRIM\033[m')

elif 9 <= idade < 14:
    print(f'o atleta tem {idade} anos.')
    print('Você é nadador \033[33mINFANTIL\033[m')

elif 14 <= idade < 19:
    print(f'o atleta tem {idade} anos.')
    print('Você é nadador \033[34mJUNIOR\033[m')

elif 19 <= idade < 25:
    print(f'o atleta tem {idade} anos.')
    print('Você é nadador \033[35mSÊNIOR\033[m')

else:
    print(f'o atleta tem {idade} anos.')
    print('Você é nadador \033[31mMASTER\033[m')

sleep(2)
print('-=' * 20)
print('ENCERRANDO...')
sleep(1.5)
print('-=' * 20)