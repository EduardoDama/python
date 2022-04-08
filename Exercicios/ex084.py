pessoas = []
dados = []
maior = menor = 0
print('-=-=-=-=-=-= Cadastro de pessoas medindo peso -=-=-=-=-=-=')
while True:
    dados.append(input('nome: '))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    if maior == 0:
        maior = menor = dados[1]

    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    dados.clear()
    v = ''
    while v != 'S' and v != 'N':
        v = input('Quer continuar?: [S/N]').upper()[0]
    if v == 'N':
        break
    print('-=' * 25)
print('-=' * 25)
print(f'Você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso lido foi de {maior}Kg, peso de', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0].capitalize()}]', end=' ')
print(f'\nO menor peso lido foi de {menor}Kg, peso de', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0].capitalize()}]', end=' ')
