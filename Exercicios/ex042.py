from time import sleep
print('\033[31m-=-=-=-=-=-= \033[36mFerificação de Triangulo\033[31m -=-=-=-=-=-=\033[m')
r1 = float(input('Qual é o comprimento do primeiro lado? '))
r2 = float(input('Qual é o comprimento do segundo lado? '))
r3 = float(input('Qual é o comprimento do terceiro lado? '))
print('\033[31m-=' * 24)

n1 = r1 == r2
n2 = r1 == r3
n3 = r2 == r3
n4 = r2 == r1
n5 = r3 == r2
n6 = r3 == r1
n10 = n1 + n2 + n3 + n4 + n5 + n6


print('\033[33mCALCULANDO...')
print('\033[31m-=\033[m' * 24)
sleep(1)
if (r1 + r2) > r3 and (r3 + r2) > r1 and (r1 + r3) > r2:
    if n10 == 6:
        print(f'Os números {r1} e {r2} e {r3} formam um triangulo \033[32mEQUILATERO\033[m')
    elif n10 == 2:
        print(f'os números {r1} e {r2} e {r3} formam um triangulo \033[32mISOSCELES\033[m')
    elif n10 == 0:
        print(f'os números {r1} e {r2} e {r3} formam um triangulo \033[32mESCALENO\033[m')
else:
    print(f'os número {r1} e {r2} e {r3} não podem formar um triangulo!')
sleep(2.5)
print('\033[31m-=' * 24)
print('\033[33mENCERRANDO...')
print('\033[31m-=' * 24)
sleep(0.5)
print('\033[36mTenha um bom dia!')
print('\033[31m-=\033[m' * 24)
