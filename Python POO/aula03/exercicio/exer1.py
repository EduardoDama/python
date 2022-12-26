import json

class Cidade:
    def __init__(self, nome, idade, prefeito):
        self.nome = nome
        self.idade = idade
        self.prefeito = prefeito

ci1 = Cidade('Gama', 68, 'Eduardo')
ci2 = Cidade('São Paulo', 125, 'Erasmo Carlos')
ci3 = Cidade('Paris', 354, 'Mbappé')

cidades = [vars(ci1), vars(ci2), vars(ci3)]  
with open('python POO/aula03/exercicio/classe.json', 'w', encoding='utf-8') as my_json:
    json.dump(cidades, my_json)




