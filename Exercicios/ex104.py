def leiaInt(msg):
    while True:
        v = input(msg)
        if not v.isnumeric():
            print('\033[31mERRO, tente novamente!\033[m')
        else:
            return int(v)
        


n1 = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n1}')
