impares = 0
solicitado = 0
for c in range(1, 501, 2):
        if c % 3 == 0:
            impares += c
            solicitado += 1
print(f'A soma de todos os {solicitado} valores solicitados é {impares} ')
