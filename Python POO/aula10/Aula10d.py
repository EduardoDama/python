class Multiplicar: #Classe decoradora
    def __init__(self, multilicador):
        self.multilicador = multilicador

    def __call__(self, func):
        def interno(*args, **kwargs):
            res = func(*args, **kwargs)

            return res * self.multilicador
        
        return interno



@Multiplicar(9) #Decorator
def somar(x, z):
    return x + z
print(somar(3, 9))