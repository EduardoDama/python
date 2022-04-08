import random
n1 = input('Qual é o primeiro nome:')
n2 = input('Qual é o segundo nome: ')
n3 = input('Qual é o terceiro nome :')
n4 = input('Qual é o Quarto nome: ')
nomes = [n1,  n2, n3, n4]
random.shuffle(nomes)
print(f'a ordem de apresentação será {nomes}' )