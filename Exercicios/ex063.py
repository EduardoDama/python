from time import sleep
print('-=-=-=-=-=-= Sequencia de finonacci -=-=-=-=-=-=')
sequencia = int(input('Quantos termos você quer da sequencia de Fibonacci?:  '))
c = 0
n1 = 0
n2 = 1
n3 = 0
while c <= sequencia:
    c += 1
    if c != 1:
        print(n1, end=' -> ')
        sleep(0.1)
    n3 += n1
    n1 = n3
    n3 = n2
    n2 = n1
print('Fim...')
print('-=' * 24)
print('tenha bom dia!')
print('-=' * 24)
