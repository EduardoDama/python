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
    def __init__(self, cliente):
        self.cliente = cliente
        self._agencias = [159357, 258456, 268431, 416896]
        self._clientes = ['Eduardo', 'Galinzé', 'Chupas', 'Coranto']
        self._numero = [2165456, 6561651, 7564656, 1191662]

    def sacar(self):
        dadosConta = self.cliente.conta.__dict__
        if dadosConta['num'] in self._numero:
            if dadosConta['agen'] in self._agencias:
                if self.cliente.nome in self._clientes:
                    self.cliente.conta.sacar()
        else:
            print('dados errados')

    def depositar(self):
        self.cliente.conta.depositar()


conta1 = contaCorrente(2165456, 159357, 1000)
cl1 = Cliente('Eduardo', 15, conta1)

bank1 = banco(cl1)

bank1.sacar()

bank1.depositar()




