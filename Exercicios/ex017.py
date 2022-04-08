import math
co = float(input('qual é o comprimento do cateto oposto: '))
ca = float(input('Qual é o comprimento do cateto adjacente: '))
n1 = math.hypot(co , ca)
print(f'O comprimento do cateto oposte é {co} o adjacente é {ca} e a hipotenusa e {n1:.2f}')