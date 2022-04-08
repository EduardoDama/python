from time import sleep
def lin():
    print('-='*20)
def maior(*valor):
    lin()
    numero = 0
    print('Analizando os valores passados...')
    for v in valor:
        if v > numero:
            numero = v
        print(v, end=' ')
        sleep(0.5)
    print(f'Foram informados {len(valor)} valores ao todo.')
    print(f'O maior valor informado foi {numero}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
