from time import sleep
numero = int(input('Digite um número e mostraremos se ele é par ou impar: '))
n1 = numero % 2
print('PROCESSANDO...')
sleep(1)
if n1 == 1:
    print(f'O número {numero} é impar!!')
else:
    print(f'O numero {numero} é par!!')