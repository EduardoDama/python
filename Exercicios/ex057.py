sexo = ''
c = 1
print('-=-=-=-=-=-= CADASTRO -=-=-=-=-=-=')
while sexo != 'M' and sexo != 'F':
    if c == 1:
        nome = input('Qual é seu nome? ')
        idade = int(input(f'Qual a idade de {nome}?'))
    c += 1
    sexo = input(f'Qual o sexo do {nome}? [M/F]').strip().upper()[0]

    if sexo != 'M' and sexo != 'F':
        print('Sexo invalido! Tente novamente.')
    print('-=' * 20)
print(f'Tenha um bom dia!! {nome}!')
print('-=' * 20)