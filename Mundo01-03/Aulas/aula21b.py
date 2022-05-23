def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: primeiro valor
    :param b: segundo valor
    :param c: terceiro valor
    Função criada por HSK from Corujes.
    """
    s = a + b + c
    print(f'A soma vale {s}.')


somar(5, 3, 6)
somar(5, 3)
somar(5)
somar()
somar(c=4, a=2)
