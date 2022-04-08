palavras = 'aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', \
           'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro'
print('-=-=-=-=-=-= LOCALIZANDO AS VOGAIS -=-=-=-=-=-=', end='')
for c in palavras:
    print(f'\nNa palavra {c.upper()} Temos ', end='')
    q = len(c)
    for vogais in c:
       if vogais.lower() in 'aeiou':
           print(vogais, end=' ')
print('\n', end='')
print('-=' * 20)
