nome = input('Qual o seu nome? ')
sobrenome = input('Qual o seu sobrenome? ')
anoNas = int(input('Qual o seu ano de nascimento? '))
altura = float(input('Qual a sua altura? '))

idade = 2023 - anoNas

maiorIdade = idade >= 18

print('-='*20)
print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', anoNas)
print('É maior de idade?', maiorIdade)
print('Altura em metros:', altura)
print('-='*20)
