from math import trunc
from time import sleep
print('\033[33m-=-=-=-=-=-=\033[m \033[36mSISTEMA DE NOTAS\033[m \033[33m-=-=-=-=-=-=\033[m')
nota1 = float(input('Qual foi a primeira nota? '))
nota2 = float(input('qual foi a segunda nota? '))
resultado = (nota1 + nota2) / 2
print('\033[33m-=\033[m' * 20)
print('PROCESSANDO NOTAS...')
print('\033[33m-=\033[m' * 20)
sleep(1.5)

if trunc(resultado) >= 7:
    print(f'Sua media foi {resultado:.1f}, isto é, \033[34mAPROVADO\033[m')
elif trunc(resultado) <= 6.9 and trunc(resultado) >= 5:
    print(f'Sua media foi {resultado:.1f}, isto é, \033[35mRECUPERAÇÃO\033[m')
else:
    print(f'Sua media foi {resultado:.1f}, isto é, \033[31mREPROVADO\033[m')
sleep(1.5)
print('\033[33m-=\033[m' * 20)
print('ENCERRANDO...')
sleep(1.5)
print('\033[33m-=\033[m' * 20)
