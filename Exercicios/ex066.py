n = c = s = 0
print('-=-=-=-=-=-= NÚMEROS -=-=-=-=-=-=')
while True:
    n = int(input('Digite um número: [999 para parar]  '))
    if n == 999:
        break
    else:
        c += 1
        s += n
print(f'''Foram digitados {c} números
O somatorio de todos os números é {s}''')
print('-=' * 16)