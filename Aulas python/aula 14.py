n = 1
contadorPar = 0
contadorImpar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        contadorPar += 1
    else:
        contadorImpar += 1
print(f'O total de números impares deu {contadorImpar} e de pares é {contadorPar}')