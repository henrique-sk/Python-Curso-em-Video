dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos Km rodados? '))
total = (dias * 60) + (km * .15)
print('O total a pagar é de R${:.2f}.'.format(total))