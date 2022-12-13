class Pessoa():
    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

p1 = Pessoa('Eduardo', 'Damasceno', 14)

print(f'O nome é {p1.nome} o sobrenome é {p1.sobrenome} e sua idade é {p1.idade}')

