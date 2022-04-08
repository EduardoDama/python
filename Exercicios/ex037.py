from time import sleep
print('-=-=-=-=-=-=BASE DE CONVERSÃO-=-=-=-=-=-= ')
n1 = int(input('Qual número você deseja converter?: '))
print('''\033[33m[1]\033[m PARA BINARIO
\033[33m[2]\033[m PARA OCTAL
\033[33m[3]\033[m PARA EXADECIMAL''')

n2 = int(input('Qual conversão você quer?: '))
print('-=' * 21)
print('\033[31mPROCESSANDO...\033[m')
sleep(1.5)
if n2 == 1:
      n3 = bin(n1).replace('b', '')
      print(f'O número {n1} em binario dá {n3[2:]}')
elif n2 == 2:
      n3 = oct(n1)
      print(f'O número {n1} em Octal é {n3[2:]}')
elif n2 == 3:
      n3 = hex(n1)
      print(f'O número {n1} em hexadecimal dá {n3[2:]}')
else:
      print('opção invalida!!, tente novamente.')
print('\033[31mENCERRANDO...\033[m')
sleep(1.5)
print('-=' * 21)



