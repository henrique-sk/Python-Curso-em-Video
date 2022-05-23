n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print('Asoma vale {}.'.format(n1+n2))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}.\nE tem mais...'.format(s, m, d), end=' ')
# o 'end' diz o que vai ter no final, se '', não quebra a linha
# \n quebra a linha
print('A divisão inteira é {} e a potência é {}.'.format(di, e))