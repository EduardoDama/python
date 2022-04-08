matriz = [[], [], []]
cont = 0
somatot = somaterceira = maior  = 0
print('-=-=-=-=-=-= MATRIZ -=-=-=-=-=-=')
for c in range(0, 3):
    for i in range(0, 3):
        valor = int(input(f'Digite um valor para {c, i}: '))
        if c == 0:
            matriz[0].append(valor)
        elif c == 1:
            matriz[1].append(valor)
        else:
            matriz[2].append(valor)
print('-=' * 16)
for m in matriz:
    for n in m:
        print(f'[  {n}  ]', end=' ')
    print()
for m in matriz:
    #Soma de todos os pares
    for n in m:
        if n % 2 == 0:
            somatot += n
    #soma dos valores da terceira coluna
    somaterceira += m[-1]
    #O maior valor da segunda linha
    if m == matriz[1]:
         for n in m:
             if maior == 0:
                 maior = n
             else:
                 if n > maior:
                     maior = n
print(end='')
print('-=' * 16)
print(f'''A soma dos valores pares é {somatot}.
A soma dos valores da terceira coluna é {somaterceira}.
O maior valor da segunda linha é {maior}.''')
