listagem = 'lápis', 1.75, 'borracha', 2.00, 'caderno', 15.90, 'estojo', 25.00,\
           'transferidor', 4.20, 'compasso', 9.99, 'mochila', 120.32, 'canetas', 22.30, \
           'livro', 34.90
print('-=' * 20)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-=' * 20)
for c in range(0, len(listagem)):
    if c % 2 == 0:
       print(f'{listagem[c]:.<30} ', end='')
    else:
        print(f'R$ {listagem[c]:>5.2f}')

print('-=' * 20)
