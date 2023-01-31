from abc import ABC, abstractmethod


class log(ABC):
    @abstractmethod
    def log(self, msg): ...

    def erro_log(self, msg):
        return self.log(f'ERRO: {msg}')

    def sucesso_log(self, msg):
        return self.log(f'SUCESSO: {msg}')


class logPrintMixin(log):
    def log(self, msg):
        print(f'{msg} (LogPrint)')


l = log()