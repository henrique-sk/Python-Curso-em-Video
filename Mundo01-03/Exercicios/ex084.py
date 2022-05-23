lista = []
dado = []
maisP = maisL = 0
while True:
    dado.append(input('Nome: '))
    dado.append(float(input('Peso: ')))
    if not lista:
        maisP = maisL = dado[1]
    else:
        if dado[1] > maisP:
            maisP = dado[1]
        if dado[1] < maisL:
            maisL = dado[1]
    lista.append(dado[:])
    dado.clear()
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar? [S/N] ')\
            .upper().strip().replace(' ', '')
    if resposta in 'N':
        break
print(f'{"-="*30}'
      f'\nAo todo, você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {maisP:.1f}Kg. Peso de ', end='')
for pessoa in lista:
    if pessoa[1] == maisP:
        print(f'[{pessoa[0]}] ', end='')
print(f'\nO menor peso foi de {maisL:.1f}Kg. Peso de ', end='')
for pessoa in lista:
    if pessoa[1] == maisL:
        print(f'[{pessoa[0]}] ', end='')
