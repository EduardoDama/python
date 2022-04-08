'''from random import randint
from time import sleep
num = []
def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        sorteio = randint(1, 10)
        print(sorteio, end=' ')
        num.append(sorteio)
        sleep(0.5)
    print('Feito!')
def somaPar(num):
    print('Somando os valores pares de', end=' ')
    totpar = 0
    for v in num:
        if v % 2 == 0:
            totpar += v
            print(f'\033[32m{v}\033[m', end=' ')
        else:
            print(f'\033[31m{v}\033[m', end=' ')
    print(f'temos {totpar}')


sorteia()
somaPar(num)'''


def somar(a=0, b=0, c=0, d=0):
    s = a + b + c + d
    return s


print(somar(5, 6, 8, 9))
print(somar(2, 3, 6))
print(somar(2, 9))
print(somar(2))

