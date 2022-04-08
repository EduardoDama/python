from ex108 import moeda
print('-=' * 20)
num = float(input('Digite um preço R$ '))
print('-=' * 20)
print(f'A aumentando 10% temos {moeda.formatacao(moeda.aumentar(num, 10))}')
print(f'Dimiuindo 13% temos {moeda.formatacao(moeda.diminuir(num, 13))}')
print(f'A metade de {moeda.formatacao(num)} é {moeda.formatacao(moeda.metade(num))}')
print(f'O dobro de {moeda.formatacao(num)} é {moeda.formatacao(moeda.dobro(num))}')
print('-=' * 20)
