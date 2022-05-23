from math import sqrt, floor, ceil
# import math
num = int(input('Digite um número: '))
# raiz = math.sqrt(num)
raiz = sqrt(num)
# print('A raiz de {} é igual a {}.'.format(num, math.ceil(raiz)))
print('A raiz de {} é igual a {}.'.format(num, ceil(raiz)))
# print('A raiz de {} é igual a {}.'.format(num, math.floor(raiz)))
print('A raiz de {} é igual a {}.'.format(num, floor(raiz)))
# ceil arredonda para cima, floor para baixo