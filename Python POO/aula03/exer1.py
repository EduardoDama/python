class Cidade:
    def __init__(self, nome, idade, prefeito):
        self.nome = nome
        self.idade = idade
        self.prefeito = prefeito


ci = Cidade('Gama', 68, 'Eduardo')

dados = ci.__dict__
