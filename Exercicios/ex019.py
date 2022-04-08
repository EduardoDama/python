import random
nome1 = input('Qual é o primeiro nome: ')
nome2 = input('Qual é o segundo nome: ')
nome3 = input('Qual é o terceiro nome: ')
nome4 = input('Qual é o quarto nome: ')
nomes = [nome1, nome2, nome3, nome4]
nome = random.choice(nomes)
print(f'os nomes foram {nome1, nome2, nome3 , nome4}')
print(f'Quem limpará o quadro será ({nome})')