from random import randint
computador = randint(1, 10)
palpite = 0
c = 1
print('-=-=-=-=-=-=-=-=-=-= JOGO DA ADIVINHAÇÃO -=-=-=-=-=-=-=-=-=-=')
print('O computador pensou em um número entre (1 e 10), tente acertar.')
palpite = int(input('qual será o palpite? '))
print('-=' * 20)
while palpite != computador:
    if palpite > computador:
        print('MENOS...')
    elif palpite < computador:
        print('MAIS...')
    palpite = int(input('Qual será o novo palpite? '))
    c += 1
    print('-=' * 20)
print(f'''PARABÉNS!! Você acertou
Você tentou {c} vezes''')
print('-=' * 20)
