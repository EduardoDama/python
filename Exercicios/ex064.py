n = 0
cont = 0
soma = 0
print('-=-=-=-=-=-= SOMADOR DE NÚMEROS -=-=-=-=-=-=')
while n != 999:
    n = int(input('Digite um número [999 parar o programa]  '))
    if n != 999:
        cont += 1
        soma += n
    print('-=' * 20)
print(f'''o total de números digitados é {cont} 
E a soma deles totalizou {soma}.''')
