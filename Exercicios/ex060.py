# solução usando o comando WHILE
print('-=-=-=-=-=-= CALCULO DE FATORIAL -=-=-=-=-=-=')
fatorial = int(input('Qual será o número para mostrarmos o seu fatorial? '))
verificação = ''
while verificação != 'N':
    print('-=' * 20)
    c = 0
    m = fatorial
    multiplicar = fatorial
    while c < fatorial - 1:
        c += 1
        m -= 1
        multiplicar *= m

    print(f'o fatorial de {fatorial}! =  {multiplicar}')
    print('-=' * 20)
    verificação = input('Quer continuar? [S/N]: ').upper()
    print('-=' * 20)
    if verificação == 'S':
        fatorial = int(input('Qual será o novo fatorial para calcularmos? '))
print('-=' * 20)
print('Tenha um bom dia!!')
print('-=' * 20)


# solução usando o comando FOR
'''print('-=-=-=-=-=-= CALCULO DE FATORIAL -=-=-=-=-=-=')
fatorial = int(input('Qual será o fatorial para calcularmos? '))
multiplicar = fatorial
for c in range(fatorial - 1, 0, -1):
    multiplicar *= c
print('-=' * 20)
print(multiplicar)
print('-=' * 20)
print('Tenha um bom dia!')
print('-=' * 20)'''
