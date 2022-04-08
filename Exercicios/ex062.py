from time import sleep
print('-=-=-=-=-=-= PROGREÇÃO ARITMEDICA -=-=-=-=-=-=')
inicio = int(input('Qual será o inicio da PA?: '))
razao = int(input('Qual será a razão da PA?:'))
c = 0
soma = inicio
n = 0
print('-=' * 20)
resp = 'S'
número = 10
stot = 10
while número != 0:
    n += 1
    if n >= 2:
        print('PAUSA...')
        número = int(input('Quantos números a mais você quer que mostre?: '))
        c = 0
        stot += número
#else:
#número = int(input('Quantos digitos você quer que mostre?:  '))
#stot = número
    while c < número:

        print(soma, end=' -> ')
        c += 1
        soma += razao
        sleep(0.1)

print(F'A PA foi finalizada com {stot} termos mostrados')
print('FIM...')
