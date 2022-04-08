numeros = list()
maior = 0
menor = 0
u = 0
print('-=' * 30)
print(f'{"Valores em Lista":^60}')
print('-=' * 30)
for c in range(0, 5):
    numeros.append(int(input(f'Qual será o valor para a posição {c}: ')))
for n in numeros:

    if u == 0:
        maior = n
        menor = n
    else:
        if n >= maior:
            maior = n
        if n <= menor:
            menor = n
    u += 1
print('-=' * 30)
print(f'Você digitou os seguintes números {numeros}')
print(f'O maior valor é {maior} e encontra-se nas posições', end=' ')
for p, c in enumerate(numeros):
    if c == maior:
        print(f'{p}...', end=' ')
print(f'\nO menor valor é {menor} e encontra-se nas posições', end=' ')
for p, c in enumerate(numeros):
    if c == menor:
        print(f'{p}...', end=' ')
