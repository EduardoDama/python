from time import sleep
from math import trunc
print('-=-=-=-=-=-= MEDIDOR DE IMC -=-=-=-=-=-=')
peso = float(input('Qual é seu peso?: '))
altura = float(input('Qual seu altura?: '))
print('-=' * 20)
imc1 = (peso / altura**2)
imc = trunc(imc1)
print('AGUARDE O CALCULO DO PESO...')
print('-=' * 20)
sleep(1)
if imc < 18.5:
    print(f'O seu IMC é de {imc} e é considerado BAIXO PESO')
elif imc >= 18.5 and imc < 25:
    print(f'O seu IMC é de {imc} e é considerado peso IDEAL')
elif imc >= 25 and imc < 30:
    print(f'O seu IMC é de {imc} e é considerado SOBREPESO')
elif imc >= 30 and imc < 40:
    print(f'O seu IMC é de {imc} e é considerado OBESIDADE')
else:
    print(f'O seu IMC é de {imc} e é considerado OBESIDADE MORBIDA')
print('-=' * 20)
sleep(0.5)
print('ENCERRANDO CÓDIGO...')
print('-=' * 20)
sleep(1)
print('Tenha um bom dia!!')
print('-=' * 20)