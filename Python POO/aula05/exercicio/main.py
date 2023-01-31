class carro:
    def __init__(self, nome):
        self.nome = nome 
        self.motor = None
        self.frabricante = None

    @property
    def nomeCarro(self):
        return self.nome


    def InserirMotor(self, motorzão):
        self.motor = motorzão.nome


    def inserirFabricante(self, tycoon):
        self.frabricante = tycoon.nome

    def mostrar(self):

        print(f'{self.nome}: tem o motor {self.motor} e é da frabricante {self.frabricante}')



class motor:
    def __init__(self, nome):
        self.nome = nome

class fabricante:
    def __init__(self, nome):
        self.nome = nome



carro1 = carro('Celta')

motor1 = motor('biturbão')

fabricante1 = fabricante('Chevrolet')

carro1.InserirMotor(motor1)

carro1.inserirFabricante(fabricante1)



carro2 = carro('Ferrari')



fabricante2 = fabricante('Ferrari')

motor2 = motor('biturbão Ferrari')

carro2.inserirFabricante(fabricante2)
carro2.InserirMotor(motor2)


carro1.mostrar()

carro2.mostrar()
