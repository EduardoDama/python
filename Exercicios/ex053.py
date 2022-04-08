inverso = ''
frase = input('Digite uma frase: ').replace(' ', '')
original = frase
for c in range(len(frase) -1,  -1, - 1):
    inverso += frase[c]
print(f'A frase original é {original} e ela invertida é {inverso}')
if inverso == frase:
    print('Temos um PALINDROMO')
else:
    print('não temos um PALÍNDROMO')

