números = 'Zero', 'um', 'dois', 'três', 'Quatro', 'cinco', 'seis',\
          'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',\
          'Quatorze', 'Quinze', 'Dezesseis', 'dezessete', 'dezoito', \
          'dezenove', 'vinte'
continuação = ''
print('-=' * 20)
print('{:^40}'.format('NÚMEROS POR EXTENSO'))
print('-=' * 20)
print('ESCREVA UM NÚMERO ENTRE 0 E 20')
print('-=' * 20)
while True:
    usuario = int(input('Qual será o número para mostrarmos por extenço?: '))
    if 0 <= usuario <= 20:
        print('-=' * 20)
        print(f'Número {usuario} em extenço é {números[usuario].upper()}')
        print('-=' * 20)
        while continuação != 'S' and continuação != 'N':
            continuação = input('Quer continuar? [S/N] ').upper()[0]
        if continuação == 'N':
            break
        continuação = ''
        print('-=' * 20)
    else:
        print('tente novamente! ')
        print('-=' * 20)
print('-=' * 20)
print('Volte sempre!!')
print('-=' * 20)
