import moeda
print('-=' * 20)
num = float(input('Digite um preço: R$'))
print('-=' * 20)
print(f'A metade de R${num} é R${moeda.metade(num)}')
print(f'O dobro de R${num} é R${moeda.dobro(num)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(num, 10)}')
print(f'Diminuindo 13%, temos R${moeda.dimunuir(num, 13)}')
