primeiroTermo = int(input('Vamos fazer uma PA.'
                          '\nDigite o primeiro termo  dessa PA: '))
razão = int(input('Digite a razão para essa PA: '))
print('Os 10 primeiros termos da PA são:')
termo = primeiroTermo
c = 0
while c < 10:
    print('{} -> '.format(termo), end='')
    c += 1
    termo += razão
print('FIM!')
