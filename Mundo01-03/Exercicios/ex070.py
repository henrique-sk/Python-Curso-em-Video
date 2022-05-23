print(40 * '-')
print('{:^40}'.format('LOJA SUPER BARATÃO'))
print(40 * '-')
total = thousandplus = cheaper = count = 0
cheaperN = ' '
while True:
    name = input('Nome do Produto: ')
    price = float(input('Preço: R$'))
    count += 1
    total += price
    if price > 1000:
        thousandplus += 1
    if count == 1 or cheaper > price:
        cheaper = price
        cheaperN = name
    # else:
    #     if cheaper > price:
    #         cheaper = price
    #         cheaperN = name
    answer = ' '
    while answer not in 'SN':
        answer = input('Quer continuar? [S/N]')\
            .upper()[0].strip().replace(' ', '')
    if answer == 'N':
        break
print('{:-^38}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}.'
      f'\nTemos {thousandplus} produtos custando'
      f' mais de R$1000.00.'
      f'\nO produto mais barato foi {cheaperN}'
      f' que custa R${cheaper:.2f}.')

