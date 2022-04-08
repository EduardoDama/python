estado = {}
brasil = []
for c in range(0, 3):
    estado['Uf'] = input('Unidade Federativa: ')
    estado['Sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
