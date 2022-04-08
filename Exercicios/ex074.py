from random import randint
maior = 0
menor = 0
números = randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5)
print('-=-=-=-=-=-= SORTEADOR DE NÚMEROS -=-=-=-=-=-=')
for c in números:
   if maior == 0:
       maior = números[0]
       menor = números[0]
   else:
       if c > maior:
           maior = c
       elif c < menor:
           menor = c

print(f'Os números sorteados foram: ', end='')
for c in números:
    print(c, end=' -> ')
print('\n', end='')
print('-=' * 20, end='')
print(f'''\nO maior deles foi {maior}
E o menor deles foi {menor}''')
print('-=' * 20)