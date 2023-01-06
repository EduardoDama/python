class Person:
    ano = 2023 # atributo de classe

    def __init__(self, name, yearsOld):
        self.name = name
        self.idade = yearsOld
    
    @classmethod #Método de classe (FACTORIES)
    def criar_50_anos(cls, nome): #Primeiro parâmetro cls
        return cls(nome, 50)

    @classmethod
    def criar_anonimo(cls, idade):
        return cls('Anônima', idade)


p1 = Person.criar_50_anos('Eduardo')
p2 = Person.criar_anonimo(25)

print(p1.name, p1.idade)
print(p2.name, p2.idade)
