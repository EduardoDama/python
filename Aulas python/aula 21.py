def contador(i, f, p):
    """
    -> fAZ UMA CONTAGEM E MOSTRA NA TELA.
    :param i: INÍCIO DA CONTAGEM
    :param f: fIM DA CONTAGEM
    :param p: PASSO DA CONTAGEM
    :return: SEM RETORNO
    Função criada por Eduardo Damasceno
    """
    for c in range(i, f + 1, p):
        print(c, end=' -> ')
    print('FIM!')
help(contador)




