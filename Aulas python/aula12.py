nome = input('Qual é seu nome? ').title()

if nome == 'Eduardo':
    print('Que nome lindo!!')
elif nome == 'Fernada' or nome == 'Milson' or nome == 'Margarida' or nome == 'Fernando' or nome == 'Mateus':
    print('Seu nome é bem popular no Brasil')
else:
    print('Seu nome é bem comum no Brasil.')

print(f'Tenha um bom dia, {nome}!')