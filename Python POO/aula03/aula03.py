class Animal:

    edu = 'Eduardo' #escopo

    def __init__(self, nome):
        self.nome = nome

    def comer(self, alimento):
        return f'o {self.nome} está comendo {alimento}'





cachorro = Animal('Cachorro')

print(cachorro.nome)
print(cachorro.comer('Frango'))
