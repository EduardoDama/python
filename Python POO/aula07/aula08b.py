from abc import ABC, abstractmethod

class Classe(ABC):
    def __init__(self, nome):
        self._nome = nome
        self.nome = nome

    @property #Getter
    def nome(self): 
        return self._nome

    @nome.setter
    @abstractmethod
    def nome(self, nome): ...


class subClass(Classe):
    nome = ''

    def __init__(self, nome):
        super().__init__(nome)

    @Classe.nome.setter
    def nome(self, nome): 
        self._nome = nome
        



niam = subClass('Adnas')
print(niam.nome)