s = 0
c1 = 0
print('-=-=-=-=-=-= SOMA DOS NÚMEROS PARES -=-=-=-=-=-=')
for c in range(1, 7):
    n = int(input(f'Digite o {c}° número: '))
    if n % 2 == 0:
        s += n
        c1 += 1
    print('-=' * 20)
print(f'A quantidade de números pares é {c1} e o somatorio dos números é {s}')
print('-=' * 20)
