print('-=-=-=-=-=-= TABUADA V3 -=-=-=-=-=-=')
tabuada = input('qual será a tabuada para mostrarmos')
c = 1

while True:

    if c == 11:
        print('-=' * 20)
        tabuada = input('Qual será a outra tabuada para mostrarmos?  ')
        print('-=' * 20)
        c = 1
        if '-' in tabuada:
            break

    print(f'{int(tabuada)} X {c} = {int(tabuada) * c}')
    c += 1
print('-=' * 20)
print('Fim...')
print('-=' * 20)
