import json
from exer1 import Cidade


with open('python POO/aula03/exercicio/classe.json') as my_json:
    arquivo = json.load(my_json)

ci1 = Cidade(**arquivo[0])
ci2 = Cidade(**arquivo[1])
ci3 = Cidade(**arquivo[2])

print(ci1.nome)
print(ci2.idade)
print(ci3.prefeito)