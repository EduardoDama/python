from abc import abstractmethod, ABC
class conta(ABC):
    def __init__(self, num, agen, sald):
        self.num = num
        self.agen = agen
        self.sald = sald

    @abstractmethod
    def sacar(self, valor):
        print(f'sacando, {valor}R$')
        print(f'Valor no banco é {self.sald}R$')
        print('-='*20)

    @abstractmethod
    def depositar(self, valor):
        print(f'despositando, {valor}R$')
        print(f'Valor no banco é {self.sald}R$')
        print('-='*20)

class contaPoupança(conta):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
    
    def sacar(self, valor):
        if valor > 1000:
            print('Não se pode tirar um valor acima de 1000$')
        else:
            self.sald -= valor
            super().sacar(valor)

    def depositar(self, valor):
        if valor > 2000:
            print('Não se pode colocar um valor acima de 2000R$')
        else:
            self.sald += valor
            super().depositar(valor)
            

class contaCorrente(conta):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
    
    def sacar(self, valor):
        if valor > 2500:
            print('Não se pode tirar um valor acima de 2500$')
        else:
            self.sald -= valor
            super().sacar(valor)

    def depositar(self, valor):
        if valor > 8000:
            print('Não se pode colocar um valor acima de 8000$')
        else:
            self.sald += valor
            super().depositar(valor)




