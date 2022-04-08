r1 = float(input('diga o comprimento de uma reta: '))
r2 = float(input('diga o comprimento da segunda reta: '))
r3 = float(input('diga o comprmento da terceira reta: '))
r1NEW = (r2 + r3) > r1
r2NEW = (r1 + r3) > r2
r3NEW = (r2 + r1) > r3
r4NEW = r1NEW + r2NEW + r3NEW
if r4NEW == 3:
    print(f'os números {r1}, {r2}, {r3} podem formar um triangulo!!')
else:
    print('não podem formar um triangulo!!')

