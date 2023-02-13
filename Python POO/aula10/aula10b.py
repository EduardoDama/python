def Myrepr(cls):
    def RPR(self):
        return f'{self.__class__.__name__} {self.__dict__}'

    cls.__repr__ = RPR
    return cls
        
def MyPlanet(metodo):
    def NomePlanet(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        if self.nome == 'Terra':
            print('Bem Vindo a Casa')
        else:
            print('Bem vindo ao planeta extraterrestre')
        return resultado

    return NomePlanet
@Myrepr
class Time:
    def __init__(self, nome):
        self.nome = nome

@Myrepr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @MyPlanet
    def Falar_nome(self): 
        return f'O Planeta é {self.nome}'


flamengo = Time('Flamengo')
Brasil = Time('Brasil')


Terra = Planeta('Terra')
Plutão = Planeta('Plutão')


print(Brasil)
print(flamengo)
print(Terra.Falar_nome())
print(Plutão.Falar_nome())