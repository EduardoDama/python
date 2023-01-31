from log import logFileMixin as logar

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False 

    def ligar(self):
        if not self._ligado:
            self._ligado = True

    def desligar(self):
        if self._ligado:
            self._ligado = False


class Celular(Eletronico, logar):
    def ligar(self):
        super().ligar()
        msg = f'Ligando {self._nome}'
        self.sucesso_log(msg)

    def desligar(self):
        super().desligar()
        msg = f'Desligando {self._nome}'
        self.erro_log(msg)
