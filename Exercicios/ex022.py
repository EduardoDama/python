nome = input('Qual é seu nome completo? ').strip()
nome2 = nome.split()
nome3 = ''.join(nome2)
segundo = nome2[0]
terceiro = len(segundo)
nome4 = len(nome3)

print(f"""ANALIZANDO NOME...
seu nome em maiusculas é {nome.upper()}
seu nome em minusculas é {nome.lower()}
o total de letras sem considerar os espaços {nome4}
o total de caracteres do primeiro nome é {terceiro}""")
