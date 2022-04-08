from time import sleep
print('-=-=-=-=-=-= MENU DE OPÇÕES -=-=-=-=-=-=')
n1 = int(input('Qual será o primeiro valor? '))
n2 = int(input('Qual será o segundo valor? '))
print('-=' * 20)
escolha = 0
while escolha != 5:
    print('''ESCOLHA UM DELES PARA PROSSEGUIR
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS VALORES
[5] SAIR DO PROGRAMA''')
    escolha = int(input(': '))
    print('-=' * 20)
    if escolha == 1 or escolha == 2 or escolha == 3 or escolha == 4 or escolha == 5:

        if escolha == 1:
            soma = n1 + n2
            print(f' {n1} + {n2} = {soma}')
        elif escolha == 2:
            multiplicar = n1 * n2
            print(f'{n1} X {n2} = {multiplicar}')
        elif escolha == 3:
            if n1 > n2:
                print(f'O número {n1} é maior que {n2}.')
            elif n2 > n1:
                print(f'o número {n2} é maior que {n1}.')
            else:
                print(f'Os números {n1} e {n2} são iguais')
        elif escolha == 4:
            n1 = int(input('Qual será o novo primeiro valor? '))
            n2 = int(input('Qual será o novo segundo valor? '))
        print('-=' * 20)
    else:
        print('Opção invalida! tente novamente')
        print('-=' * 20)
    sleep(1.5)

print('Tenha um bom dia!')
print('-=' * 20)
