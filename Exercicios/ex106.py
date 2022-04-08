c = ('\033[m', '\033[31m', '\033[34m', '\033[35m', '\033[40;7m')
def ajuda(esco):
    print(c[4])
    help(esco)
    print(c[0], end='')

def titulo(msg, cor):

    print(c[cor], end='')
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))
    print(c[0], end='')


while True:
    titulo('  SISTEMA DE AJUDA pyHELP  ', 2)
    escolha = input('Função ou biblioteca ("fim" interrompe)> ').lower()
    if escolha == 'fim':
        titulo('  ATÉ LOGO!  ', 1)
        break
    titulo(f'  Acessando o manual do comando \'{escolha}\'  ', 3)
    ajuda(escolha)

