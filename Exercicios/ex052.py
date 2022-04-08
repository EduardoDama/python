from time import sleep
divisivel = 0
print('-=-=-=-=-=-= VERIFICADOR DE NÚMEROS PRIMOS -=-=-=-=-=-=')
primo = 0
contador = int(input('Qual é o número que você quer saber?: '))
for c in range(1, contador + 1):
   if contador % c == 0:
       primo = primo + 1
       color = f'\033[32m{c}\033[m'
       print(color, end = ' ')
       divisivel += 1
   else:
       color = f'\033[31m{c}\033[m'
       print(color, end = ' ')

if primo == 2:
    print(f'''
o número {contador} foi divisivel {divisivel} vezes!
por isso ele é um número PRIMO!''')

else:
    print(f'''
O número {contador} foi divisivel {divisivel} vezes!
por isso ele não é um número primo!!''')

print('-=' * 27)
sleep(1)
print('tenha um bom dia!')
print('-=' * 27)
