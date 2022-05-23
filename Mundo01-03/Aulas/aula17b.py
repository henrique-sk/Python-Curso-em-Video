valores = [] # ou valores = list()
for cont in range(0, 3):
    valores.append(int(input('Digite um valor: ')))

for chave, valor in enumerate(valores):
    print(f'Na posição {chave} encontrei o valor {valor}!')
print('Cheguei ao final da lista.')
