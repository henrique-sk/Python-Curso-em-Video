n = int(input('Digite um número: '))
d = n * 2
t = n * 3
print('O dobro de {} é {}.\nO triplo é {}.\nE a raiz quadrada é {:.2f} ou {:.5f}.'.format(n, d, t, (n ** (.5)), pow(n, (1/2))))