num = list()
verificação = 'S'
print('-=' * 30)
print(f'{"Valores Em Listas":^60}')
print('-=' * 30)
while True:
    if verificação == 'S':
        valor = int(input('Digite um valor: '))
        if valor not in num:
            print('Valor adicionado com sucesso!!')
            num.append(valor)
        else:
            print('Valor duplicado! Não vou adicionar...')
    else:
        break

    verificação = ''
    while verificação != 'S' and verificação != 'N':
        verificação = input('Quer continuar? [S/N] ').upper()[0]
print('-=' * 30)
print(f'Você digitou os números {sorted(num)}')
print('-=' * 30)
