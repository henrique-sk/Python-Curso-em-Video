n = int(input('Digite um número inteiro para ver sua tabuada: '))
l = 12 * '-'
print(l)
for i in range(1, 11):
    print('{} x {:2} = {}'.format(n, i, i * n))
print(l)
