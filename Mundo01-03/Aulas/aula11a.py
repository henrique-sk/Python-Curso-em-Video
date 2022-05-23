print('\033[1;33;40mEste texto é colorido\33[m')
print('\033[7;33;40mEste codigo inverte a cor\33[m')
a = 3
b = 5
print('Os valores são \033[32;40m{}\33[m e \033[31m{}\33[m'.format(a, b))
nome = 'Henrique'
print('Olá {}{}{}!!'.format('\33[4;34m', nome, '\33[m'))
cores = {'limpa':'\33[m',
         'azul':'\33[34m',
         'amarelo':'\33[33m',
         'pretoebranco':'\33[7;30m'}
print('Olá {}{}{}!!'.format(cores['pretoebranco'], nome, cores['limpa']))
