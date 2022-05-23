def sorteia(lista):
    from random import randint as ri
    from time import sleep as sl
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        lista.append(ri(1, 10))
        print(f'{lista[c]} ', end='')
        sl(.2)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {lista}, temos {soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)
