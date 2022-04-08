somatorio = 0
maisVelho = 0
soma = 0
maisNova = 0
print('-=-=-=-=-=-= ANALIZADOR COMPLETO -=-=-=-=-=-=')
for c in range(0, 4):
    nome = input('Qual é seu nome?: ')
    idade = int(input(f'Qual é a idade de {nome}?: '))
    sexo = input(f'Qual é o sexo do/da {nome} [F/M]?: ').upper()
    somatorio +=  idade
    if sexo == 'M':
        if idade > maisVelho:
            maisVelho = idade
            maisVelhoNome = nome
    if sexo == 'F':
        if idade < 20:
            soma += 1
    print('-=' * 20)
media = somatorio / 4
print(f'''A media das idade resultou em ({media})
O nome do homem mais velho E ({maisVelhoNome.upper()} com {maisVelho} anos)
E a quantidade de meninas com menos de 20 anos é ({soma})''')
print('-=' * 20)