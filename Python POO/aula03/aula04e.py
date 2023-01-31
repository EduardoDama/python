class caneta:
    def __init__(self, cor, tampa):
        self._cor = cor
        self._corTampa = tampa
    
    @property
    def cor(self):
        print('Getter')
        return self._cor

    @cor.setter
    def cor(self, newColor):
        print('Setter')
        self._cor = newColor

    @property
    def cor_tampa(self):
        print('Getter')
        return self._corTampa

    @cor_tampa.setter
    def cor_tampa(self, newColorTamp):
        print('Setter')
        self._corTampa = newColorTamp

c1 = caneta('Azul', 'Vermelha')

c1.cor = 'Verde'

c1.cor_tampa = 'Lilás'

print(f'Cor da caneta {c1.cor} cor da tampa {c1.cor_tampa}')