numero = float(input('Qual é o seu salario atual?: R$ '))
por = float(input('Quantos porcento o seu salario aumentará?: '))
calc3 = (por / 100) * numero + numero
print(f'O seu novo salario será de {calc3:.2f} R$')