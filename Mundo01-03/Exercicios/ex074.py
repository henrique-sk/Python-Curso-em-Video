from random import randint

valores = randint(0, 10), randint(0, 10),\
          randint(0, 10), randint(0, 10),\
          randint(0, 10)
print('Os valores sorteados foram: ', end='')
for i in valores:
    print(i, end=' ')
print(f'\nO maior valor sorteado foi {max(valores)}.'
      f'\nO menor valor sorteado foi {min(valores)}.')
