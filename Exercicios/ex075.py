print('-=-=-=-=-=-= VERIFICADOR DE NÚMEROS -=-=-=-=-=-=')
números = (int(input('Digite um valor: ')),
          int(input('Digite outro valor: ')),
          int(input('Digite mais um valor: ')),
          int(input('Digite o último valor: ')))
print('-=' * 20)
print(f'O valor 9 apareceu {números.count(9)} vezes.')
if números.count(3) == 0:
    print('O valor 3 apareceu em nenhuma posição.')
else:
    print(f'O valor 3 apareceu na posição {números.index(3) + 1}ª')
print('Os números pares são: ', end='')
for c in números:
    if c % 2 == 0:
        print(c, end=' ')
print('\n', end='')
print('-=' * 20)
