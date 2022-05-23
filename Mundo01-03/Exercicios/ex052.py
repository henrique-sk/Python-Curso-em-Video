num = int(input('Digite um número inteiro: '))
cont = 0
amostra = []
for i in range(1, num + 1):
    if num % i == 0:
        cont += 1
        amostra += [i]
if cont == 2:
    print('O número {} só é divisível por {} e {}'
          ', portanto é primo!'.format(num, amostra[0], amostra[1]))
else:
    print('O número {} é divisível pelos números {}'
          ', portanto não é primo!'.format(num, amostra))
