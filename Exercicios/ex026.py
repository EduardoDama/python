letra = str(input('Escreva uma frase: ')).lower().strip()
letra2 = letra.find('a')
letra3 = letra.rfind('a')
letra4 = letra.count('a')

print(f"""o total de letra A é {letra4}
A primeira aparição da letra A foi {letra2 + 1}
A ultima aparição da letra A foi {letra3 + 1}""")

