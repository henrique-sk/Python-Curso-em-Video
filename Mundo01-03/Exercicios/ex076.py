listagem = 'Lápis', 1.75, 'Borracha', 2,\
           'Caderno', 15.9, 'Estojo', 25,\
           'Transferidor', 4.2,\
           'Compasso', 9.99, 'Mochila', 120.32,\
           'Canetas', 22.3, 'Livro', 34.9
print(40 * '-')
print(f'{"LISTAGEM DE PREÇOS":^40}')
print(40 * '-')
for c in range(0, len(listagem), 2):
    print('{:.<30}R$'.format(listagem[c]), end='')
    print('{:>7.2f}'.format(listagem[c+1]))
print(40 * '-')
