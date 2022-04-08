def aumentar(n=0, t=0):
    res = ((t / 100) * n) + n
    return res


def diminuir(n=0, t=0):
    res = n - (t / 100) * n
    return res


def dobro(n=0):
    res = n * 2
    return res


def metade(n=0):
    res = n / 2
    return res


def formatacao(valor=0, format='R$'):
    return f'{format}{valor:.2f}'.replace('.', ',')



