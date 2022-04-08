cont = 0
exp = list()
print('-=-=-=-=-=-= Expressão Númerica -=-=-=-=-=-=')
exp.append(input('Digite um expressão numerica: '))
for c in str(exp):
    if c == '(' or c == ')':
       cont += 1
if cont % 2 == 0:
    print('Sua expressão está correta!')
else:
    print('Sua espressão está errada!')

