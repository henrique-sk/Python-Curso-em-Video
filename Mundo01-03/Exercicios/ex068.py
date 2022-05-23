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
    while parImpar not in 'PARÍMPAR':
        parImpar = input('Par ou Ímpar? [P/I]: ').strip()\
            .upper()[0].replace(' ', '').replace('P', 'PAR')\
            .replace('I', 'ÍMPAR')
    if soma % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print(30 * '-',
          f'\nVocê jogou {valor} e o computador {valorPc}.'
          f' Total de {soma}, DEU {resultado}!')
    print(30 * '-')
    if resultado == parImpar:
        c += 1
        print('Você VENCEU!'
              '\nVamos jogar novamente...')
    else:
        print('Você PERDEU!')
        print(15 * '=-')
        print(f'GAME OVER! Você venceu {c} vezes.')
        break
