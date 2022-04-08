
from time import sleep
print('-=-=-=-=-=-= SISTEMA DE PAGAMENTO -=-=-=-=-=-=')
preco = float(input('Qual é o valor do produto? '))
print('-=' * 23)
print(''' ESCOLHA A FORMA DE PAGAMENTO!
[1] A vista no dinheiro
[2] A vista no cartão
[3] parcelado''')
FormaDePagamento = int(input(' '))
if FormaDePagamento == 1 or FormaDePagamento == 2 or FormaDePagamento == 3:
    if FormaDePagamento != 3:
        print('-=' * 23)
        print('CALCULANDO OS VALORES...')
        print('-=' * 23)
        sleep(1)

    if FormaDePagamento == 1:
        desconto = (10 / 100) * preco
        precoReal = preco - desconto
        print(f'O desconto foi de {desconto}')
        print({f'O valor atualizado será de {precoReal}'})

    elif FormaDePagamento == 2:
        desconto = (5 / 100) * preco
        precoReal =  preco - desconto
        print(f'''O desconto será de {desconto} 
    E o preço atualizado será de {precoReal}''')

    elif FormaDePagamento == 3:
        print('-=' * 23)
        parcelas = int(input('Quantos parcelas será?: '))
        print('-=' * 23)
        if parcelas <= 2:
            print(f'o preço continuará o mesmo R${preco}')
        elif parcelas > 2:
            aumento = (preco * 20 / 100)
            precoReal =  preco + aumento
            valorPorMes = precoReal / parcelas
            print(f''' o aumento será de {aumento} 
    O valor atualizado será de {precoReal}
    E o valor mensal será de {valorPorMes}''')
            print('-=' * 23)
else:
    print('Forma de pagamento invalida!!, tente novamente')
sleep(3)
print('-=' * 23)
print('Tenha um bom dia!')
print('-=' * 23)
