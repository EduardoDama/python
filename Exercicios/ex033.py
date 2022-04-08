a = int(input('escreva o primeiro número: '))
b = int(input('Escreva o segundo número: '))
c = int(input('escreva o terceiro número: '))
menor = c
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
maior = c
if b > a and b > c:
     maior = b
if a > b and a > c:
     maior = a

print(f'o maior número é {maior}')
print(f'O menor número é {menor}')
