def lin():
    print('-=' * 20)
def area(a, b):
    print(f'A área de um terreno {a} X {b} é de {a*b}M²')


# Codigo principal
lin()
print('   CONTROLE DE TERRRENOS  ')
lin()
lar = float(input('Largura do terreno: [M] '))
com = float(input('Comprimento do terreno: [M] '))
lin()
area(lar, com)
