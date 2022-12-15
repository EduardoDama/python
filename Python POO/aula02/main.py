class produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, porcentual):
        self.preco = self.preco - (self.preco * (porcentual / 100))
        print(self.preco)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, name):
        self._nome = name.title()



    #getter
    @property
    def preco(self):
        return self._preco

    #setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
            
        self._preco = valor

p = produto('COMPUTADOR', 'R$95') 
p.desconto(10)

print(p.nome)