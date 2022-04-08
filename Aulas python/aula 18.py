galera = []
dado = []
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(input('Qual seu nome?: '))
    dado.append(int(input('Qual sua idade?: ')))
    galera.append(dado[:])
    dado.clear()
for i in galera:
    if i[1] >= 20:
        print(f'{i[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{i[0]} é menor de idade')
        totmenor += 1

print('-=' * 20)
print(f'O total de pessoas maiores de idade são {totmaior}\n'
      f'O total de pessoas menor de idade são {totmenor}')