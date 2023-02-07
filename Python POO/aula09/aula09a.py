class Ponto:
    def __init__(self, x, y, z='string') -> None:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str: #Retorna string mostrando o valor
        return f'{self.x} e {self.y}'

    def __repr__(self) -> str: #__repr__ = representar o objeto, desenvolvedor
        nome_classe = self.__class__.__name__
        return f'{nome_classe}[x={self.x!r} e y={self.y!r}, z={self.z!r}]' # Mostrar o tipo do parâmetro


p1 = Ponto(159, 15)

print(repr(p1))

print(str(p1))