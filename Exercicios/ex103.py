def ficha(n, g):
    if not n.isalpha():
        n = '<desconhecido>'
    if not g.isnumeric():
        g = 0
    else:
        int(g)
    return f'O jogador {n} fez {g} gol(s) no campeonato.'


nome = input('nome do jogador: ').strip()
gols = input(f'Quantos gols fez?: ').strip()
print(ficha(nome, gols))
