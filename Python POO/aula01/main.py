from pessoa import Pessoa


p1 = Pessoa.por_ano_nas('eduardo', 2008)

print(p1.nome, p1.idade)

print('ID:', p1.gera_id())