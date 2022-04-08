jogador = {}
gols = []
print('-=-=-=-=-=-= ESTATISTICA DE UM JOGADOR -=-=-=-=-=-=')
jogador['Nome'] = input('Nome do jogador?: ')
jogos = int(input(f'Quantos partidas {jogador["Nome"]} jogou?: '))
for c in range(1, jogos + 1):
    gol = int(input(f'  -> Quantos gols na partida {c}°?: '))
    gols.append(gol)
jogador['Gols'] = gols[:]
jogador['Total'] = sum(gols)
print('-=' * 20)
print(jogador)
print('-=' * 20)
for k, v in jogador.items():
    print(f'No campo {k} tem o valor {v}.')
print('-=' * 20)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for p, v in enumerate(gols):
    if v > 1:
        print(f'   => Na partida {p + 1}, fez {v} gols.')
    else:
        print(f'   => Na partida {p + 1}, fez {v} gol.')
print(f'foi um total de {jogador["Total"]} gols')
