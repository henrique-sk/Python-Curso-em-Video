print('Os números ípares e múltiplos de 3 no intervalo ente 1 e 500 são:')
soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        soma += i
        cont += + 1
        print(i, end=' ')
print('\nSão ao todo {} números, que somados entre si totaliza {}.'.format(cont, soma))
