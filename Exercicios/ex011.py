largura = float(input('Qual é a largura de sua parede?: '))
altura = float(input('Qual é a  altura de sua parede?: '))
area = largura * altura
pintura = area / 2
galao = pintura / 3
print(f'Sabemos que a altura é {altura} e sua largura é {largura} sua área é {area}m² ')
print(f'E a quantidade de litros de tinta para pintar esta parede é {pintura:.2f}L ')
print(f'E gastaria galões de tinta {galao:.0f} ')
