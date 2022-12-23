class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def Ano_nas(self):
        return self.Ano_atual - self.idade 


p1 = Pessoa('Eduardo', 14)
p2 = Pessoa('Jubscrevalda', 97)


dados = {'nome': 'Jubscrevalda', 'idade': 97}
p1 = Pessoa(**dados)#astesristico serve para abrir(desempacotar)
print(p1.idade)
