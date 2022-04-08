num = list()
n = 0
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c == 0:
        num.append(valor)
        print(f'o valor {valor} foi adicionado no final da lista!!')
    else:
        if valor == 0 or valor > num[-1]:
            num.append(valor)
            print(f'o valor {valor} foi adicionado no final da lista!!')
        else:
            pos = 0
            while pos < len(num):
                if valor <= num[pos]:
                    num.insert(pos, valor)
                    print(f'O valor {valor} foi adicionado na posição {pos}')
                    break
                pos += 1
print(num)


