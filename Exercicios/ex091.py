from random import randint
from time import sleep
from operator import itemgetter
jogos = {}
ranking = {}
print('-=-=-=-=-=-= JOGO DO DADO -=-=-=-=-=-=')
for c in range(1, 5):
    jogos[f'jogador{c}'] = randint(1, 6)
print('valores sorteados:')
for k, v in jogos.items():
    print(f' - O {k} tirou {v} no dado.')
    sleep(0.5)
ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('-=' * 20)
print('======== RANKING DOS JOGADORES ======== ')
for p, v in enumerate(ranking):
    print(f'   {p + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.5)
