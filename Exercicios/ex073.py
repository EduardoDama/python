from time import sleep
times = 'Atlético-MG', 'Flamengo', 'Palmeiras', 'Bragantino', 'Corinthians',\
        'Fortaleza', 'Internacional', 'Fluminense', 'América-MG', 'Ceará', 'Santos', \
        'Cuiabá', 'Athletico-PR', 'Atlético-GO', 'São Paulo', 'Juventude', 'Bahia', \
        'Grêmio', 'Sport', 'Chapecoense'

print('-=' * 20)
print('{:^40}'.format('TABELA DO BRASILEIRÃO 2021'))
print('-=' * 20)

cont = 0
print('A tabela é: ')
print('-=' * 20)

for c in times:
        cont += 1
        print(f'{cont} {c}')
sleep(2)

print('-=' * 20)
print('os cinco primeiros são: ')
print('-=' * 20)
time5 = times[:5]
cont = 0

for c in time5:
        cont += 1
        print(f'{cont} {c}')

sleep(3)
print('-=' * 20)
print('Os quatros ultimos são: ')
print('-=' * 20)
timeZ4 = times[16:]
cont = 16

for c in timeZ4:
    cont += 1
    print(f'{cont} {c}')
sleep(2.5)
print('-=' * 20)
print('Na ordem alfabetica é: ')
print('-=' * 20)

alfaTime = sorted(times)
for c in alfaTime:
        print(c)
sleep(3)
print('-=' * 20)
print(f'E a Chapecoense está na {times.index("Chapecoense") + 1}° posição')
print('-=' * 20)
sleep(1)
print('Tenha um bom dia!')
print('-=' * 20)

