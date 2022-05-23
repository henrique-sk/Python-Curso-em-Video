from random import randint
from time import sleep

r = randint(0,5)
num = int(input('Estou pensando em um número inteiro entre 0 e 5, adivinhe qual é: '))
print('PROCESSANDO...')
sleep(3)
frase = 'O número que eu pensei é'
if r == num:
    print(frase, '{}! Parabéns! Você adivinhou!'.format(r))
else:
    print(frase, '{}! Você errou!'.format(r))
