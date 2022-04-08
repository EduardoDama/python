from random import randint
from time import sleep
resultado = randint(0, 2)
itens = ('papel', 'tesoura', 'pedra')

print('-=-=-=-=-=-= JOGO DO JOKENPÔ -=-=-=-=-=-=')
print('''[0] papel
[1] tesoura
[2] pedra''')
usuario = int(input('Qual escolerá?: '))
if usuario == 0 or usuario == 1 or usuario == 2:
    print('-=' * 21)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!!!')
    sleep(0.5)
    print('-=' * 21)

    if usuario == resultado:
        print(f'empate, o computador jogou {itens[resultado]}')

    if usuario == 0 and resultado == 1:
        print(f'computador venceu, ele jogou {itens[resultado]}')

    if usuario == 1 and resultado == 0:
        print(f'você venceu, o computador jogou {itens[resultado]}')

    if usuario == 2 and resultado == 0:
        print(f'computador venceu, ele jogou {itens[resultado]}')

    if usuario == 0 and resultado == 2:
        print(f'você venceu, o computador jogou {itens[resultado]}')

    if usuario == 1 and resultado == 2:
        print(f'computador venceu, ele jogou {itens[resultado]}')

    if usuario == 2 and resultado == 1:
        print(f'você venceu, o computador jogou {itens[resultado]}')
else:
    print('Opção invalida, tente novamente.')
print('-=' * 21)
