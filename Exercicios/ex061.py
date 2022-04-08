from time import sleep
print('-=-=-=-=-=-= PROGRESSÃO ARITMEDICA -=-=-=-=-=-=')
inicio = int(input('Qual será o inicio da PA?: '))
razao = int(input('Qual será a razão da PA?:'))
c = 0
soma = inicio
print('-=' * 20)
while c < 10:
    print(soma, end=' -> ')
    c += 1
    soma += razao
    sleep(0.1)
print('FIM...')
