from time import sleep
def lin():
    print('-=' * 20)
def contador(i, f, p):
    lin()
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2)
    if i < f:
        for v in range(i, f+1, p):
            print(v, end=' ')
            sleep(0.5)
        print('Fim!')
    elif i > f:
        for v in range(i, f-1, -p):
            print(v, end=' ')
            sleep(0.5)
        print('Fim!')
        lin()

#codigo principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)
