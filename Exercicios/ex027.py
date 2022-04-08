nome = str(input('Qual é seu nome completo? ')).title().strip().split()
print(f"""seu nome é {' '.join(nome)}
seu primeiro nome é {nome[0]}
Seu ultimo sobrenome é {nome[len(nome) - 1]}""")
