class Carro:
    def __init__(self, nome, cor, ano, potência, velocidade):
        self.nome = nome
        self.cor = cor
        self.ano = ano
        self.potência = potência
        self.velocidade = velocidade


    def acelerar(self):
        print(f'O {self.nome} está acelerando...')

    def desacelerar(self):
        print(f'O {self.nome} está desacelerando...')

    def idade(self):
       idade =  2022 - self.ano  
       return idade

    def veloz(self):
        if self.velocidade > 80:
            return 'Acima da velocidade, MULTADO'
        else:
            return 'Velocidade normal, Tenha um bom dia!'


celta = Carro('Celta', 'Vermelho', 2000, 50, 60)
print(f'Carro 1 é uma {celta.nome}')

celta.acelerar()

print(celta.idade(), 'Anos')

print(celta.veloz())


ferrari = Carro('Ferrari', 'Preta', 2021, 525, 125)
print(f'Carro 2 é uma {ferrari.nome}')

ferrari.desacelerar()

print(ferrari.idade(), 'Anos')

print(ferrari.veloz())
