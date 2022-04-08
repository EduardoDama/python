tot = 0
resp = 'S'
maisdeMil = 0
maisBarato = 0
nomeBarato = ''
print('-=' * 20)
print('           LOJA SUPER BARATÃO         ')
print('-=' * 20)
while True:
    if resp == 'S':
        nome = input('Qual é o nome do produto?: ')
        preço = int(input('Qual é o preço do produto?: R$ '))
        resp = ''
        print('-=' * 20)
        if tot == 0:
            maisBarato = preço
            nomeBarato = nome
        tot += preço
        if preço >= 1000:
            maisdeMil += 1
        if preço < maisBarato:
            maisBarato = preço
            nomeBarato = nome
        while resp != 'S' and resp != 'N':
            resp = input('Quer continuar?: [S/N] ').upper()[0]
            if resp != 'S' and resp != 'N':
                print('Opção invalida!! Tente novamente.')
                print('-=' * 20)
    else:
        break
    print('-=' * 20)
print('COMPRA FINALIZADA...')
print('-=' * 20)
print(f'''O total do compra foi de {tot}
O total de produtos que custaram mais de 1000 foi {maisdeMil}
E o nome do produto mais barato foi {nomeBarato.upper()} e custou {maisBarato}''')
print('-=' * 20)
