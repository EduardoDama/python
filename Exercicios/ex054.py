maiores = 0
menores = 0
from datetime import date
ano = date.today().year
print('-=-=-=-=-=-= CONTADOR DE DATA DE NASCIMENTO -=-=-=-=-=-=')
for c in range(1, 8):
    anoNas = int(input(f'digite o ano de nascimento da {c}° pessoa?: '))
    if ano - anoNas >= 18:
        maiores += 1
    else:
        menores += 1
print('-=' * 20)
print(f'''dessas pessoas {maiores} são maiores de idade, e  {menores} são menores.''')
print('-=' * 20)
