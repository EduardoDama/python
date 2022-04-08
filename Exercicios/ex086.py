matriz = [[], [], []]
print('-=-=-=-=-=-= MATRIZ -=-=-=-=-=-=')
for c in range(0, 3):
    for i in range(0, 3):
        valor = int(input(f'Digite um valor para [{c}, {i}]: '))
        if c == 0:
            matriz[0].append(valor)
        elif c == 1:
            matriz[1].append(valor)
        else:
            matriz[2].append(valor)
print('-=' * 16)
for m in matriz:
    for n in m:
        print(f'[{n:^5}]', end=' ')
    print()

