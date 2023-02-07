class Ponto:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str: #__repr__ = representar o objeto, desenvolvedor
        nome_classe = self.__class__.__name__
        return f'{nome_classe}[x={self.x!r} e y={self.y!r}]' # Mostrar o tipo do parâmetro

    def __add__(self, outro):
        new_x = self.x + outro.x
        new_y = self.y + outro.y
        return Ponto(new_x, new_y) #Criar um objeto com a soma

    def __gt__(self, outro): #Maior que
        new_x = self.x + self.y
        new_y = outro.x + outro.y
        return new_x > new_y # Return True ou False


p1 = Ponto(5, 8)
p2 = Ponto(7, 2)

p3 = p1 + p2
print(p3)
print(p1 > p2)