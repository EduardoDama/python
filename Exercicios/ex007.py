nome = input('Qual é o nome do aluno: ')
no1 = float(input(f'Qual foi a primeira nota do {nome}: '))
no2 = float(input(f'Qual foi a segunda nota do aluno {nome}: '))
no3 = float(input(f'Qual foi a terceira nota do {nome}: '))
no4 = float(input(f'Qual foi quarta nota do {nome}: '))
media1 = (no1 + no2 + no3 + no4) / 4
print(f'A media do aluno anual do {nome} é {media1:.1f}')