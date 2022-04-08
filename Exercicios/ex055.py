peso = 0
peso1 = 0
peso3 = 5000
maior = 0
menor = 2121

print('-=-=-=-=-=-= VERIFICADOR DE PESO -=-=-=-=-=-=')
for c in range(0, 6):
    if c < 5:
        peso = peso1
        peso1 = float(input('Digite aqui o seu peso: '))
        print('-=' * 20)
    if peso1 > maior:
        maior = peso1
    if peso1 <= menor:
        menor = peso1

print(f'''O maior peso digitado foi {maior} KG
O menor peso digitado foi {menor} KG''')
print('-=' * 20)
