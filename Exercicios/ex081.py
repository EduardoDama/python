num = list()
v = ''
print('-=-=-=-=-=-= Dados na Lista -=-=-=-=-=-=')
while True:
    num.append(int(input('Digite um valor: ')))
    while v != 'S' and v != 'N':
        v = input('Quer continuar? [S/N] ').upper()[0]
    if v == 'N':
        break
    v = ''
print('-=' * 30)
if 5 not in num:
    print('O valor 5 Não foi digitado.', end='')
else:
    print('O número 5 foi digitado nas posições:', end=' ')
    for p, n in enumerate(num):
        if n == 5:
            print(f'{p}...', end=' ')
print(f'\nVocê digitou {len(num)} elementos.')
num.sort(reverse=True)
print(f'Os valores em ordem decrescente são {num}')
