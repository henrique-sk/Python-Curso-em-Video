lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar? [S/N] ')\
                .upper().strip().replace(' ', '')
    if resposta == 'N':
        break
pares = list()
impares = list()
for index, valor in enumerate(lista):
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
print(30 * '-=')
print(f'A lista completa é {lista}'
      f'\nA lista de pares é {pares}'
      f'\nA lista de ímpares é {impares}')
