pessoas = []
pessoa = {}
totIdade = 0
print('-=-=-=-=-=-= CADASTRO DE PESSOAS -=-=-=-=-=-=')
while True:
    pessoa['Nome'] = input('Nome: ')
    pessoa['Idade'] = int(input('Idade: '))
    while True:
        pessoa['Sexo'] = input('Sexo: [M/F]').upper()[0]
        if pessoa['Sexo']in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoas.append(pessoa.copy())
    totIdade += pessoa['Idade']
    pessoa.clear()
    while True:
        v = input('Quer continuar?: [S/N] ').upper()[0]
        if v in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')

    if v == 'N':
        break
    print('-=' * 20)
media = totIdade / len(pessoas)
print('-=' * 20)
print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A media de idade é de {media:.2f} anos.')
print('- As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['Sexo'] == 'F':
        print(p['Nome'], end=' ')
print('\n- Lista das pessoas que estão acima da média: ')
for p in pessoas:
    if p['Idade'] > media:
        for k, v in p.items():
            print(f'  {k} = {v};', end=' ')
        print()
print('<< ENCERRANDO >>')
