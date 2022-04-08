from datetime import date
from time import sleep
ano = int(input('Que ano você quer analizar? Ou coloque 0 para analizar o ano atual: '))
sleep(0.5)
if ano == 0:
    ano = date.today().year
if ano % 4 == 0:
    print(f'O ano {ano} é um ano BISSEXTO!!')
else:
    print(f'O ano {ano} não é um ano BISSEXTO!!')
