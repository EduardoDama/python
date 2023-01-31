class Pessoa:
    Ano_atual = 2022 #atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def Ano_nas(self):
        return self.Ano_atual - self.idade 


p1 = Pessoa('Eduardo', 14)
p2 = Pessoa('Jubscrevalda', 97)
print(p1.Ano_nas())
print(p2.Ano_nas())
