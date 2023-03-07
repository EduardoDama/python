from banco import *
from contas import conta
class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def name(self):
        return self.nome
    
    @name.setter
    def name(self, nome):
        self.nome = nome
        
    @property
    def years(self):
        return self.idade
    
    @years.setter
    def years(self, idade):
        self.idade = idade 
    

    

    

class Cliente(pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta: conta | None = None