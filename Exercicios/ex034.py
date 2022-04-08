salario = float(input('Qual é seu salario?: '))
if salario >= 1250.00:
    calculo = salario + (salario * 10 / 100)
    print(f'Seu salario sofrerá um aumento de 10%, e será de {calculo}')

else:
    calculo = salario + (salario * 15 / 100)
    print(f'Seu salario sofrerá um aumento de 15%, e será de {calculo}')

