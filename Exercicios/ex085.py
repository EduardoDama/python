numeros = [[], []]
print('-=-=-=-=-=-= Números pares e impares numa lista -=-=-=-=-=-=')
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print('-=' * 30)
print(f'Os valores pares digitados foram: {sorted(numeros[0])}')
print(f'Os valores impares digitados foram: {sorted(numeros[1])}')
