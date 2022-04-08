from time import sleep
r = 0
print('-=-=-=-=-=-= PROGREÇÃO ARITMEDICA -=-=-=-=-=-=')
inicio = int(input('Qual será o inicio: '))
razao = int(input('Qual será a razão: '))
print('-=' * 20)
r = inicio
for c in range(0, 10):
    print(r, end=' -> ')
    r += razao
    sleep(0.1)
print('ACABOU...')


