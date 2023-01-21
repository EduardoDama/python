'''class string(str):
    def upper(self):
        print('FUNÇÃO SOBREPOSTA')
        return super().upper()

stringer = string('Oláaaaaaaaaaa')


print(stringer.upper())'''

class A: #Apenas atributos de A
    atributo_a = 'Valor A'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('a')


class B(A): #atributos de A e B
    atributo_b = 'Valor b'

    def __init__(self, atributo, outra):
        super().__init__(atributo)
        self.outra = outra

    def metodo(self):
        print('b')


class C(B): #Atributos de A de B e C
    atributo_c = 'Valor C'

    def metodo(self):
        print('C')
        print(super().metodo())
        print(super(B, self).metodo())

c = C('Atributo', 'outra coisa')
print(c.atributo)
print(c.outra)



'''print(c.metodo())
print(C.mro())
print(B.mro())
print(A.mro())
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)'''