num = int(input('Digite um número inteiro: '))
cont = 0
for i in range(1, num + 1):
    if num % i == 0:
        print('\033[34m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')
print('\n\033[mO número {} é divisível {} vezes'.format(num, cont), end='')
if cont == 2:
    print(', portanto é primo!')
else:
    print(', portanto não é primo!')