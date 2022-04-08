from math import trunc
from time import sleep
print('-=-=-=-=-=-=SISTEMA EMPRÉSTIMO BANCARIO-=-=-=-=-=-=-')
valorCasa = float(input('Qual é o valor da casa?:R$ '))
salario = float(input('Quanto você ganha por mês? '))
anos = float(input('Em quantos anos você vai pagar?: '))
print('-=' * 26)
p = anos * 12
prestacao = valorCasa / p
porcent = (prestacao * 100 / salario)
print('PROCESSANDO...')
sleep(1.5)
if trunc(porcent) <= 30:
    print('Empréstimo \033[33mACEITO!\033[m')
    print(f'você terá de pagar por mês {prestacao:.2f}')
    print(f'Ela tirará {porcent:.2f}% porcento do seu salario.')
elif trunc(porcent) > 30:
    print(f'''Empréstimo \033[31mNEGADO\033[m
     Você terá de pagar por mês {prestacao:.2f}
     E isso passará dos 30% do seu salario
     {porcent:.2f}%''')
print('Tenha uma bom dia!!')
print('ENCERRANDO...')
print('-=' * 26)
sleep(2)


