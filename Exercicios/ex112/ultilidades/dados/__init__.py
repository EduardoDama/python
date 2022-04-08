def leiDinheiro(msg):
    while True:
        valor = input(msg).replace(',', '.').strip()
        if not valor.isnumeric() or not valor.isdecimal():
            print(f'\033[31mERRO: \"{valor}\" é um preço invalido!\033[m')
        else:
            return float(valor)


def leiaInt(msg):
    while True:
        v = input(msg)
        if not v.isnumeric():
            print('\033[31mERRO, tente novamente!\033[m')
        else:
            return int(v)
