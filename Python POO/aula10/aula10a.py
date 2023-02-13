def Myrepr(cls):
    def RPR(self):
        return f'{self.__class__.__name__} {self.__dict__}'

    cls.__repr__ = RPR
    return cls
        
@Myrepr
class Time:
    def __init__(self, nome):
        self.nome = nome

@Myrepr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


flamengo = Time('Flamengo')
Brasil = Time('Brasil')


Vênus = Planeta('Vênus')
Plutão = Planeta('Plutão')


print(Brasil)
print(flamengo)
print(Vênus)
print(Plutão)