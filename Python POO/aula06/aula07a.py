class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def fala_classe_name(self):
        print(self.nome, self.idade, self.__class__.__name__)


class Cliente(Pessoa):
    ...


c1 = Cliente('Eduardo', 14)

c1.fala_classe_name()

