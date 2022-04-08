def notas(*valor, sit=False):
    """
    -> Função onde calcula a média de vários alunos.
    :param valor: Onde entra uma ou mais notas de alunos (aceita várias notas).
    :param sit: Valor opcional, onde mostra ou não a situação.
    :return: retorna um dicionario contendo todas as informações(media, maior e menor nota, situação)
    """
    resultado = {}
    resultado['Quantidade'] = len(valor)
    resultado['Maior nota'] = max(valor)
    resultado['Menor nota'] = min(valor)
    resultado['Média'] = sum(valor) / len(valor)
    if sit:
        if resultado['Média'] < 5:
            resultado['Situação'] = 'RUIM'
        elif resultado['Média'] >= 7:
            resultado['Situação'] = 'BOA'
        else:
            resultado['Situação'] = 'RAZOAVEL'
    return resultado




print('-=' * 45)
r = notas(5.5, 2.5, 1.5, sit=True)
print(r)
print('-=' * 45)
#help(notas)
