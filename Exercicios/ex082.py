num = list()
impar = list()
par = list()
v = ''
print('-=' * 25)
print(f'{"Verificador De Números Pares e Impares":^50}')
print('-=' * 25)
while True:
    num.append(int(input('Digite um número: ')))
    while v != 'S' and v != 'N':
        v = input('Quer continuar? [S/N] ').upper()[0]
    if v == 'N':
        break
    v = ''
for n in num:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print('-=' * 25)
print(f'''A lista completa foi {num}
Os números pares dessa lista foi {par}
Os números impares dessa lista foi {impar}''')
