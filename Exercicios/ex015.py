import math
dias = int(input('por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilometros o carro percorreu? '))
dinheiro_por_dia = dias * 60
dinheiro_por_km = km * 0.15
total = dinheiro_por_km + dinheiro_por_dia
print(f'o preço diario totalizado deu ({dinheiro_por_dia}R$), e o valor por kilometro pago totalizado é ({dinheiro_por_km}R$)')
print(f'O valor totalizado é de ({total:.2F})R$')
