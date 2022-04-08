def lin():
    print('-=' * 20)
def voto(n):
    from datetime import date
    global idade
    idade = date.today().year - n
    if idade < 16:
        return 'NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'

lin()
print('SISTEMA DE VERIFICAÇÃO SE VOTA OU NÃO')
lin()

anoNas = int(input('Ano de nascimento: '))
resultado = voto(anoNas)
print(f'Com {idade} anos: {resultado}')
