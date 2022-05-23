from random import randint

c = 0
print(15 * '=-',
      '\nVAMOS JOGAR PAR OU ÍMPAR')
while True:
    valorPc = randint(0, 11)
    print(15 * '=-')
    valor = int(input('Diga um valor: '))
    soma = valorPc + valor
    parImpar = ' '
    while parImpar not in 'PI':
        parImpar = input('Par ou Ímpar? [P/I]: ').strip()\
            .upper()[0].replace(' ', '')
    print(30 * '-',
          f'\nVocê jogou {valor} e o computador {valorPc}.'
          f' Total de {soma}.')
    print('DEU PAR.' if soma % 2 == 0 else 'DEU ÍMPAR.')
    print(30 * '-')
    if parImpar == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!')
            c += 1
        else:
            print('Você PERDEU!')
            break
    elif parImpar == 'I':
        if soma % 2 != 0:
            print('Você VENCEU!')
            c += 1
        else:
            print('Você PERDEU!')
            break
    print('\nVamos jogar novamente...')
print(15 * '=-')
print(f'GAME OVER! Você venceu {c} vezes.')
