from datetime import date
from time import sleep
print('\033[33m-=-=-=-=-=-=\033[m \033[34mALISTAMENTO MILITAR\033[m \033[33m-=-=-=-=-=-=\033[m')
sexo = input('Qual é seu sexo [M/F]:').upper()
if sexo == 'M':
    anoNas = int(input('Em que ano você nasceu?: '))

    idade = date.today().year - anoNas
    print('\033[33m-=\033[m' * 22)
    print('\033[31mCALCULANDO...\033[m')
    print('\033[33m-=\033[m' * 22)
    sleep(1.5)

    if idade < 18:
        tempo = 18 - idade
        tempo2 = tempo + date.today().year
        print(f'''você ainda terá de se alistar!!
        Ainda falta {tempo} anos para se alistar.
      você terá de se alistar no ano {tempo2}''')

    elif idade == 18:
        print('Está na hora de se alistar!!')

    elif idade > 18:
        tempo = idade - 18
        tempo2 = date.today().year - tempo
        print(f'''Já passou na hora de se alistar!!
        Passou {tempo} anos de se alistar.
        o ano que deveria se alista foi em {tempo2}''')
else:
    print('Você não terá de fazer o seu alistamento miitar!!')
    print('Tenha um bom dia!')

print('\033[33m-=\033[m' * 22)
sleep(1)
print('\033[31mENCERRANDO...\033[m')
sleep(1.5)
print('\033[33m-=' * 22)