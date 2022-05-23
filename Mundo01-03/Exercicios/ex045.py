from emoji import emojize
from random import randint

itens = ('',
         emojize(':fist:', language='alias'),
         emojize(':hand:', language='alias'),
         emojize(':v:', language='alias'))
j = int(input(emojize('Vamos jogar Jokenpô!!!'
                      '\n1 - {}'
                      '\n2 - {}'
                      '\n3 - {}'
                      '\nInforme o número do que você quer jogar: '
                      .format(itens[1], itens[2], itens[3]))))
pc = randint(1, 3)
if 1 <= j <= 3:
    resultado = 'O computador jogou {0}' \
                '\nVocê jogou {1}' \
                '\nResultado:' \
                '\nVocê >> {1} x {0} << Computador'.format(itens[pc], itens[j])
                # a "\" é por estar dentro de uma variável(?)
    if (pc == 1 and j == 3) or (pc == 2 and j == 1) or (pc == 3 and j == 2):
        print(resultado, '\nVocê perdeu!')
    elif (j == 1 and pc == 3) or (j == 2 and pc == 1) or (j == 3 and pc == 2):
        print(resultado, '\nParabéns! VOCÊ GANHOU!!!')
    elif pc == j:
        print(resultado, '\nEmpatou!!!')
else:
    print('"{}" não é um valor válido.'.format(j))
