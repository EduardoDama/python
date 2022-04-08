print('-=' * 20)
print('{:^40}'.format('BANCO EDL'))
print('-=' * 20)
valor = int(input('Qual será o valor a ser retirado? '))
total = valor
ced = 50
tot = 0
print('-=' * 20)
while True:
    if total >= ced:
        total -= ced
        tot += 1
    else:
        if tot > 0:
           print(f'Você precisará de {tot} notas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tot = 0
        if total == 0:
            break
print('-=' * 20)
print('Volte sempre ao BANCO EDL! Tenha um bom dia!')
print('-=' * 20)

