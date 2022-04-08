jogadores = []
jogador = {}
gols = []
print('-=-=-=-=-=-= ESTATISTICA DE UM JOGADOR -=-=-=-=-=-=')
while True:
    jogador['Nome'] = input('Nome do jogador?: ').title()
    jogos = int(input(f'Quantos partidas {jogador["Nome"]} jogou?: '))
    for c in range(1, jogos + 1):
        gol = int(input(f'   Quantos gols na partida {c}°?: '))
        gols.append(gol)
    jogador['Gols'] = gols[:]
    jogador['Total'] = sum(gols)
    gols.clear()
    jogadores.append(jogador.copy())
    jogador.clear()
    while True:
        v = input('Quer continuar? [S/N] ').upper()[0]
        if v in 'SN':
            break
        print('ERRO, escreva apenas S ou N.')
    if v == 'N':
        break
    print('-=' * 20)
print('-=' * 20)
print('Cod ', end='')
for t in jogadores[0].keys():
    print(f'{t:<15}', end='')
print()
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
while True:
    print('-=' * 20)
    opção = 0
    opção = int(input('Escolhe uma opção: (999 interrompe)'))
    if opção == 999:
        break
    elif len(jogadores) < opção:
        print(f'Erro! Não existe um jogador com o codigo {opção}! Tente novamente.')
    else:
        print('-=' * 20)
        print(f'-- LEVANTAMENTO DO JOGADOR ({jogadores[opção]["Nome"]})')
        escolha = jogadores[opção]['Gols']
        for i, g in enumerate(escolha):
            print(' ' * 3, end='')
            print(f'Na partida {i + 1}° fez {g} gols.')
print('-=' * 20)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE! >>>')
