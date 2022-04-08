from datetime import date
pessoa = {}
anoAtual = date.today().year
print('-=-=-=-=-=-= CADASTRO DO TRABALHADOR -=-=-=-=-=-=')
pessoa['Nome'] = input('Nome: ').title()
anoNas = int(input('Ano de nascimento: '))
pessoa['idade'] = anoAtual - anoNas
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['ctps'] >= 1:
    pessoa['Contratação'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: R$ '))
    pessoa['Aposentadoria'] = pessoa['idade'] + (35 - (anoAtual - pessoa['Contratação']))
print('-=' * 20)
for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')
