from time import sleep
print('-=-=-=-=-=-COMPARAÇÃO DE DOIS NÚMEROS-=-=-=-=-=-=')
n1 = int(input('Qual é o primeiro número: '))
n2 = int(input('Qual é o segundo número: '))
print('-=' * 25)
if n1 > n2:
    print('O PRIMEIRO número  é maior!!')
elif n2 > n1:
    print('O SEGUNDO número é maior!!')
else:
    print(f'Os números {n1} e {n2} são iguais!!')
sleep(1.5)
print('\033[31mENCERRANDO...\033[m')
sleep(1.5)
print('-=' * 25)
