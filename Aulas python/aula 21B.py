def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('Digite um valor: '))
print(f'O fatorial de {n} é {fatorial(n)}')
print(fatorial(56))