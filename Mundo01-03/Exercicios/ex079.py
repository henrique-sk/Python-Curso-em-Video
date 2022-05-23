lista = []
while True:
    addValor = int(input('Digite um valor: '))
    if addValor not in lista:
        lista.append(addValor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    resposta = ' '
    while resposta not in 'SN':
        resposta = input('Quer continuar? [S/N] ')\
            .upper().strip().replace(' ', '')
    if resposta == 'N':
        break
print(26 * '-=')
print(f'Você digitou os valores {sorted(lista)}')
