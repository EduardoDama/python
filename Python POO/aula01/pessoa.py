from datetime import datetime
from random import randint

class Pessoa:

    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))


    def __init__(self, nome, idade, comendo=False, falando=False, fazendo=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.fazendo = fazendo

    #Comer
    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return

        if self.falando:
            print(f'{self.nome} Não pode comer falando')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True




    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} Não está comendo.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False




    #Falar

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return
        
        if self.falando:
            print(f'{self.nome} Já está falando')
            return

        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True




    def para_falar(self):
        if not self.falando:
            print(f'{self.nome} Já não esta falando')
            return

        print(f'{self.nome} parou de falar')
        self.falando = False

        


    def ano_nas(self):
        print(f'{self.nome} nasceu em {self.ano_atual - self.idade}') 



    @classmethod
    def por_ano_nas(cls, nome, ano_nas):
        idade = cls.ano_atual - ano_nas
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        rand = randint(1, 50)
        return rand
        
        
