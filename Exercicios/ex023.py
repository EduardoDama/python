num = int(input('Digite um numero entre 0 á 9999: '))

milhar = num // 1000 % 10
centenas = num // 100 % 10
dezenas = num // 10 % 10
unidade = num // 1 % 10

print(f"""A quantidade e milhar é {milhar}
A Quantidade de cantenas é {centenas}
A quantidade de dezenas é {dezenas}
A quantidade de unidade é {unidade}""")