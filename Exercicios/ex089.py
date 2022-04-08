from time import sleep
alunos = []
media = cont = 0
print('-=-=-=-=-=-= CALCULO DE BOLETIM -=-=-=-=-=-=')
while True:
    nome = input('Qual é o nome da aluno(A)?: ')
    n1 = float(input('Qual foi a 1° nota?: '))
    n2 = float(input('Qual foi a 2° nota?: '))
    alunos.append([nome, [n1, n2], (n1 + n2) / 2])
    v = ''
    while v != 'S' and v != 'N':
        v = input('Quer continuar? [S/N] ').upper()[0]
    if v == 'N':
        break

print('-=' * 20)
print('No. NOME           MÉDIA    ')
print('-=' * 20)
for c in alunos:
    print(f'{cont}   {c[0].title():<15}', end='')
    print(c[2])
    cont += 1
print('-=' * 20)
while True:
    v = int(input('Qual aluno você quer ver?: (999 interrompe) '))
    if v == 999:
        break
    print('-=' * 20)
    print(f'O aluno {alunos[v][0]} tirou as notas {alunos[v][1]}.')
    print('-=' * 20)
    sleep(1)
print('FINALIZANDO\n'
      '<<< VOLTE SEMPRE >>>')
