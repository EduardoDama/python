import moeda

num = float(input('Digite um preço: '))
resp = input('Quer ou não quer, com formatação: [S/N] ').upper()[0]
if resp == 'S':
    verificação = True
else:
    verificação = False
print(f'A amentando 10% temos {moeda.aumentar(num, 10, verificação)}')
print(f'Dimiuindo 13% temos {moeda.diminuir(num, 13, verificação)}')
print(f'A metade de {moeda.formatar(num)} é {moeda.metade(num, verificação)}')
print(f'O dobro de {moeda.formatar(num)} é {moeda.dobro(num, verificação)}')
