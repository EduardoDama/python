dinheiro = float(input('Quanto dinheiro você tem e vamos coverter: R$'))
dollar = dinheiro / 5.54
euro = dinheiro / 6.39
bitcoin = dinheiro / 317907
print(f'você tem {dinheiro}R$ e isso dará {dollar:.2f}US$ em euro {euro:.2f}Є e em Bitcoin dará {bitcoin:.4f}BTC')