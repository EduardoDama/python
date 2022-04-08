numero =float(input('Qual foi o valor do produto?:R$ '))
por = float(input('Qual foi o desconto do produto(sem %): '))
calc1 = por * numero
calc2 = calc1 / 100
calc3 = numero - calc2
print(f'O promoção de desconto foi de {por}%')
print(f'O desconto foi de {calc2:.2f}R$')
print(f'O valor do produto era {numero}R$ agora será de {calc3:.2f}R$')