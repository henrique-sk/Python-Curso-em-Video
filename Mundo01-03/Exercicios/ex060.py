num = int(input('Digite um número para'
                ' calcular seu fatorial: '))
c = num
total = 1
print('{}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    total *= c
    c -= 1
print('{}'.format(total))
