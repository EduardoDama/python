'''class caneta:
    def __init__(self, cor):
        self.cor = cor 

    def get_cor(self):
        return self.cor


caneta1 = caneta('Azul')
print(caneta1.get_cor())
print(caneta1.get_cor())'''

class caneta:
    def __init__(self, cor):
        self.cores = cor 

    @property
    def cor(self):
        return self.cores

    @property
    def cor_tubo(self):
        return 'Isso aí'

caneta1 = caneta('Azul')
print(caneta1.cor)

print(caneta1.cor_tubo())