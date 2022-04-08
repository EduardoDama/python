def leiaInt(msg):
    while True:
        try:
            v = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mEscrevo um número inteiro valido!\033[m')
        else:
            return v

def vermelho(msg):
    return f'\033[31m{msg}\033[m'


def azul(msg):
    return f'\033[34m{msg}\033[m'


def amarelo(msg):
    return f'\033[33m{msg}\033[m'


def lin():
    print('-=' * 20)


def menu(a):
    titulo('MENU PRINCIPAL')
    cont = 1
    for item in a:
        print(f'{amarelo(cont)} - {azul(item)}')
        cont += 1
    lin()
    try:
        resp = leiaInt(f'{amarelo("Sua opção:")} ')
    except KeyboardInterrupt:
        print('O usuario preferiu não informar.')
        return 1
    else:
        return resp


def titulo(msg):
    print('-=' * 20)
    print(msg.center(40))
    print('-=' * 20)
