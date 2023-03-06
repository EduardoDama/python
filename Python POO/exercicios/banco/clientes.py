from banco import *
class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def name(self):
        return self.nome
    
    @property
    def years(self):
        return self.idade
    

class Cliente(pessoa):
    def __init__(self, nome, idade, cont):
        super().__init__(nome, idade)
        self.conta = cont