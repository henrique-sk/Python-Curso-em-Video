num = int(input('Digite um número entre 0 e 9999: '))
u = num // 1 % 10 # se usar "% 100", pega os últimos 2 dígitos
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}:'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))