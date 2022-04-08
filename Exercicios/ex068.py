from random import randint
c = 0
print('-=-=-=-=-=-= JOGO DO PAR OU IMPAR -=-=-=-=-=-=')
usuarioN = int(input('Qual será o valor? '))
usuarioPI = input('Você vai escolher par ou impar? [P/I] ').upper()

print('-=' * 20)
while True:
    número = randint(1, 10)
    soma = número + usuarioN
    if usuarioPI == 'P':
        if soma % 2 == 0:
            print(f'O usuario Ganhou! O computador jogou {número} e totalizou {soma}')
            print('-=' * 20)
            print('CONTINUAR...')
            c += 1
            usuarioN = int(input('Qual será o valor? '))
            usuarioPI = ' '
            while usuarioPI != 'P' and usuarioPI != 'I':
                usuarioPI = input('Você vai escolher par ou impar? [P/I] ').upper()[0]
        else:
            print(f'o usuario perdeu, o computador jogou {número} e somou {soma}')
            break
    else:
        if soma % 2 == 0:
            print(f'O computador venceu! Ele jogou {número} que totalizou {soma}')
            break
        else:
            print(f'O usuario Ganhou! O computador jogou {número} e totalizou {soma}')
            print('-=' * 20)
            print('CONTINUAR...')
            c += 1
            usuarioN = int(input('Qual será o valor? '))
            usuarioPI = input('Você vai escolher par ou impar? [P/I] ').upper()
    print('-=' * 20)

print('-=' * 20)
print(f'GAMEOVER!! Você acertou concecutivamente {c}')
print('-=' * 20)

'''while True:
    nome = input('Qual é seu nome? ')
    verific = input('Quer continuar? [S/N] ').upper()[0]
    if verific == 'N':
        break'''