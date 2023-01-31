class escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, nome):
        self._ferramenta = nome


class EscreverFerramenta:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'


caneta = EscreverFerramenta('caneta')

eduardo = escritor('Eduardo')

eduardo.ferramenta = caneta

print(eduardo.ferramenta.escrever())
