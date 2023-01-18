class carro:
    def __init__(self, nome):
        self.nome = nome 
        self.motor = []
        self.frabricante = []

    @property
    def nomeCarro(self):
        return self.nome


    def InserirMotor(self, motorzão):
        self.motor.append(motorzão.nome)


    def inserirFabricante(self, tycoon):
        self.frabricante.append(tycoon.nome)

    def mostrar(self):
        print('-='*30)
        print(f'{self.nome}: tem o motor {self.motor} e é da frabricante {self.frabricante}')
        print('-='*30)


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

carro1.mostrar()

