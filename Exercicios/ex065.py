resp = 'S'
cont = 0
soma = 0
maior = 0
menor = 0
print('-=-=-=-=-=-= ANALIZADOR DE NÚMEROS -=-=-=-=-=-=')
while resp != 'N':
    número = int(input('Digite um número: '))
    if cont == 0:
        maior = número
        menor = número

    cont += 1
    soma += número

    if número > maior:
        maior = número

    elif número < menor:
        menor = número

    resp = input('Quer continuar? [S/N]  ').upper()
    print('-=' * 20)
media = soma / cont

print(f'''O maior número lido foi {maior}
O menor número lido foi {menor}
O total de números escritos foi {cont}
A soma de todos os números foi {soma}
A media foi {media:.2f}''')
print('-=' * 20)
