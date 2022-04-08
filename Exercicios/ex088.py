from random import randint
from time import sleep
numeros = []
sorteio = []
cont = 0
print('-=' * 20)
print(f'{"JOGO NA MEGA SENA":^40}')
print('-=' * 20)
vezes = int(input('Quantos jogos você quer que que sorteie? : '))
print(f'-=-=-=-=-=-= SORTEANDO {vezes} JOGOS -=-=-=-=-=-=')
for c in range(1, vezes + 1):
    for s in range(0, 6):
        valor = (randint(1, 61))
        if valor not in sorteio:
            sorteio.append(valor)
    numeros.append(sorteio[:])
    sorteio.clear()
for m in numeros:
    cont += 1
    print(f'Jogo {cont}:  {sorted(m)}')
    sleep(1)
print('-=-=-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=-=-=')
