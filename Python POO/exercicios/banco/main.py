from abc import ABC, abstractmethod

class conta(ABC):
    def __init__(self, num, agen, sald):
        self.num = num
        self.agen = agen
        self.sald = sald

    @abstractmethod
    def sacar():
        ...

    @abstractmethod
    def depositar():
        ...

class contaPoupança(conta):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
    def sacar(self):
        print('Sacando...')
        valor = int(input('Qual valor a ser retirado? '))
        if valor > 1000:
            print('Não se pode tirar um valor acima de 1000$')
        else:
            self.sald -= valor
            print('sacando...')
            print(f'Valor no banco é {self.sald}')

    def depositar(self):
        valor = int(input('Qual seria o valor a ser depositado? '))

        if valor > 2000:
            print('Não se pode colocar um valor acima de 2000R$')
        else:
            self.sald += valor
            print('despositando...')
            print(f'Valor no banco é {self.sald}')

class contaCorrente(conta):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
    
    def sacar(self):
        print('Sacando...')
        valor = int(input('Qual valor a ser retirado? '))
        if valor > 2500:
            print('Não se pode tirar um valor acima de 2500$')
        else:
            self.sald -= valor
            print('sacando...')
            print(f'Valor no banco é {self.sald}')

    def depositar(self):
        valor = int(input('Qual seria o valor a ser depositado? '))

        if valor > 8000:
            print('Não se pode colocar um valor acima de 8000$')
        else:
            self.sald += valor
            print('despositando...')
            print(f'Valor no banco é {self.sald}')




class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def name(self):
        return self.nome
    
    @property
    def years(self):
        return self.idade
    

class Cliente(pessoa):
    def __init__(self, nome, idade, cont):
        super().__init__(nome, idade)
        self.conta = cont
        
    
class banco:
    def __init__(self, cliente, conta):
        self.cliente = cliente
        self.conto = conta

conC = contaCorrente(123, 809, 0)
conP = contaPoupança(123, 809, 0)

conP.depositar()

conP.sacar()
p1 = Cliente('Eduardo', 15, conP)


