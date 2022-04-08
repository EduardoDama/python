
def aumentar(valor, porCent, verific=False):
    resp = valor + (valor * porCent / 100)
    return resp if not verific else formatar(resp)


def diminuir(valor, porCent, verific=False):
    resp = valor - (valor * porCent / 100)
    return resp if not verific else formatar(resp)


def dobro(v, verific=False):
    resp = v * 2
    return resp if not verific else formatar(resp)


def metade(v, verific=False):
    resp = v / 2
    return resp if not verific else formatar(resp)


def formatar(numero):
    return f'R$ {numero:.2f}'.replace('.', ',')


def resumo(valor=0, aument=0, reduc=0):
    print('-=' * 18)
    print(f'RESUMO DO VALOR'.center(36))
    print('-=' * 18)
    print(f'Preço analizado: \t{formatar(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aument}% de aumento: \t{aumentar(valor, aument, True)}')
    print(f'{reduc}% de redução: \t{diminuir(valor, reduc, True)}')
    print('-=' * 18)