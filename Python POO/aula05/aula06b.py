class carrinhoCompras:
    def __init__(self) -> None:
        self._produtos = []
        
    def total(self):
        return sum([p.preco for p in self._produtos])

    def inserir(self, *produto):
        for produtos in produto:
            self._produtos.append(produtos)

    def listar(self):
        print('-='*20)
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        
        print('-='*20)

class produto:
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco


car = carrinhoCompras()

p1, p2 = produto('Chevrolet', 75000), produto( 'Mansão', 1560000)

car.inserir(p1, p2)
car.listar()

print(car.total())
    