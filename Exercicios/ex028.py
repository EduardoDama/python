from random import randint
from time import sleep
numero = randint(0, 5)
print('-=-'*13)
print('TENTE ACERTER O NÚMERO QUE PENSEI')
n1USUARIO = int(input('Chute um número de 0 á 5: '))
print('-=-'*13)
print('PROCESSANDO...')
sleep(0.5)
if n1USUARIO == numero:
    print('VOCÊ VENCEU!!!')
    sleep(0.25)
else:
    print('O COMPUTADOR VENCEU!!!')
    print(f'Eu pensei no número {numero}')
    sleep(0.25)

print('FINALIZANDO...')