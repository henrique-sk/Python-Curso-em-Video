def fatorial(numero, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param numero: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor fatorial de um número numero
    """
    print(30*'-')
    fat = 1
    for c in range(numero, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= c
    return fat


print(fatorial(5, True))
help(fatorial)
