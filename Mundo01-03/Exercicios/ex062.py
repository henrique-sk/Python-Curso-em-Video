primeiroTermo = int(input('Vamos fazer uma PA.'
                          '\nDigite o primeiro termo  dessa PA: '))
razão = int(input('Digite a razão para essa PA: '))
print('Os 10 primeiros termos da PA são:')
termo = primeiroTermo
c = 0
menu = ''
qtd = 10
while c != qtd:
    print('{} -> '.format(termo), end='')
    c += 1
    termo += razão
    if c == qtd:
        menu = input('\n____________________________'
                     '\n[S] Para ver mais termos'
                     '\n[N] Para encerrar o programa'
                     '\n[S/N]: ').upper()
        if menu == 'S':
            maisTermos = int(input('Deseja ver mais quantos termos? '))
            qtd += maisTermos
print('Programa encerrado!'
      '\n{} termos mostrados.'.format(c))
