resp = 'S'
sexo = ''
maiores = 0
homens = 0
mulheres = 0
print('-=-=-=-=-=-= ANALIZE DE DADOS DO GRUPO -=-=-=-=-=-=')
while True:
    idade = int(input('Qual é a sua idade?  '))
    while sexo != 'M' and sexo != 'F':
        sexo = input('Qual é o seu sexo? [M/F] ').upper()[0]
        resp = ''
        if sexo != 'M' and sexo != 'F':
             print('Sexo invalido! tente novamente.')
             print('-=' * 25)

    print('-=' * 25)
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    sexo = ''
    while resp != 'S' and resp != 'N':
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in 'SN':
            break
        print('resposta invalida!! Tente novamente.')
        print('-=' * 20)
    if resp == 'N':
        break
    print('-=' * 25)
print(f'''O total de pessoas com mais de 18 anos é {maiores}
O total de homens cadastrados foi {homens}
O total de mulheres com menos de 20 anos é {mulheres}''')
print('-=' * 25)

