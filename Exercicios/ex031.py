km = int(input('Qual será a kilometragem de sua viagem:km '))
if km <= 200:
    valor = km * 0.50
    print(f'o valor a pagar será de {valor}R$')
else:
    valor = km * 0.45
    print(f'o valor a pagar será de {valor}R$')

