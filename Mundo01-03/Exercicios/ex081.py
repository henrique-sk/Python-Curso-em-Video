lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar? [S/N] ')\
                .upper().strip().replace(' ', '')
    if resposta in 'N':
        break
lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos.'
      f'\nOs valores em ordem decrescente são {lista}')
        # OU usar direto na str ->
        # sorted(lista,reverse=True)
if 5 in lista:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
