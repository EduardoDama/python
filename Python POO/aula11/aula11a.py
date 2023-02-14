def ReprMy(self):
    return f'{type(self).__name__} {self.__dict__}'

class MinhaMetaClasse(type):
    def __new__(mcs, name, bases, dct):
        print('ESTAMOS NO NEW DA METACLASSE')
        cls = super().__new__(mcs, name, bases, dct)

        cls.Cassarolha = 'MAMAMIA MACHELLO'

        cls.__repr__ = ReprMy

        if 'falar' not in cls.__dict__ or not callable(cls.__dict__['falar']):
            raise NotImplementedError('Coloque o método falar')
        return cls

    def __call__(self, *args, **kwargs):
        print('ESTAMOS NO CALL DA METACLASSE')
        inst =  super().__call__(*args, **kwargs)
        print(*args, **kwargs)

        if 'name' not in inst.__dict__:
            raise NotImplementedError('Coloque o nome')

        return inst

class Pessoa(metaclass=MinhaMetaClasse):
    def __new__(cls, *args, **kwargs):
        print('Estamos no NEW')
        return super().__new__(cls)

    def __init__(self, name):
        print('Estamos no INIT')
        self.name = name

    def falar(self):
        print('OIE')

    
p1 = Pessoa('Eduardo')
print(p1)

