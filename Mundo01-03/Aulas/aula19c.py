estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for estado in brasil:
    for k, v in estado.items():
        print(f'O campo {k} tem valor {v}.')
print(20*'-')
for estado in brasil:
    for v in estado.values():
        print(v, end=' ')
    print()
