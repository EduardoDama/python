print('=-=-=-=-=-=-=-=-=-=-=-=-SISTEMA DE MULTAS=-=-=-=-=-=-=-=-=-=-=-=-')
velocidade = int(input('Quantos KM/h você estava andando(sem KM)? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'VOCÊ FOI MULTADO POR ECEDER O LIMITE DE VELOCIDADE!! o valor a pagar é {multa}')

if velocidade < 45:
    multa = (60 - velocidade) * 7
    print(f'VOCÊ FOI MULTADO POR ANDAR LENTO DEMAIS!!  o valor a pagar é {multa}')

print('Dirija com segurança!! tenha um bom dia!!')


