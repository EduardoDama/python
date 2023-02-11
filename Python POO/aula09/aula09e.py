class MyOpen:
    def __init__(self, caminho, modo):
        self.caminho = caminho
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        self._arquivo = open(self.caminho, self.modo)
        return self._arquivo

    def __exit__(self, ExecaoClass, exception, traceback):
        self._arquivo.close()
        exception.add_note('Dando erro de conexão')
        raise ConnectionError('ERRO de conexão') 


arqui = MyOpen('aula09.txt', 'w')

with arqui as arquivo:
    arquivo.write('BLABLALBLA\n', 1515)
