from random import randint

pcnum = randint(0, 10)
num = -1
tentativas = 0
print('Estou pensando em um número entre 0 e 10.')
while num != pcnum:
    num = int(input('Tente adivinhar: '))
    tentativas += 1
    if num == pcnum:
        print('Parabéns! Você acertou, pensei no {}.'
              '\nAcertou na sua {}ª tentativa.'
              ''.format(pcnum, tentativas))
    else:
        if num > pcnum:
            print('Menos... Tente novamente.')
        elif num < pcnum:
            print('Mais... Tente novamente.')
