from abc import ABC, abstractmethod

class conta(ABC):
    @abstractmethod
    def sacar():
        ...

class contaPoupança(conta):
    def sacar():
        print('Sacando...')

    def deposito():
        print('despositando...')
        

class contaCorrente(conta):
    def sacar():
        print('Sacando...')

    def deposito():
        print('despositando...')




class pessoa:
    ...

class Cliente(pessoa):
    ...