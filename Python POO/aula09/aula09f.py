from contextlib import contextmanager

@contextmanager
def OpenMyFile(caminho, modo): #Função geradora
    try:
        arquivo = open(caminho, modo) #Objeto Gerador
        print('Arquivo aberto')
        yield arquivo #Retornando ao with o objeto gerador
    except Exception as erro:
        print('Ocorreu um erro!', erro)

    finally:
        print('Arquivo fechado')
        arquivo.close()
    
with OpenMyFile('aula09f.txt', 'w') as arq:
    arq.write('BLAKAJNDJANID')
