def fatorial(v, show=False):
    '''
    -> Calcula o fatorial de um número
    :param v:  O número a ser calculado.
    :param show: (opcional) Mostrar ou não o calculo.
    :return: O valor do fatorial do valor v
    '''
    fat = 1
    for c in range(v, 0, -1):
        fat *= c
        if show:
            print(c, end='')
            if c == 1:
                print(' = ', end='')
            else:
                print(' X ', end='')
    return fat
n1 = int(input('Qual é o número para calcular o fatorial?: '))
resp = input('Quer mostrar o calculo?: [S/N] ').upper()[0]
if resp == 'S':
    print(fatorial(n1, True))
else:
    print(f'O resultado é {fatorial(n1)}')

help(fatorial)

