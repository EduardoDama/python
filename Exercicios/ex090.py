aluno = {}
aluno['Nome'] = input('Nome: ')
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))
print('-=' * 20)
if aluno['Media'] < 5:
    aluno['Situação'] = 'Reprovado'
elif 5 <= aluno['Media'] < 7:
    aluno['Situação'] = 'Recuperção'
else:
    aluno['Situação'] = 'Aprovado'
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}')
