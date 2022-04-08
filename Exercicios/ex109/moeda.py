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


def formatar(numero, v=False):
    if v:
        return f'R$ {numero:.2f}'.replace('.', ',')
    return numero