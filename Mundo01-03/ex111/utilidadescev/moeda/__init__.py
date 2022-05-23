def aumentar(preco=0, taxa=0, form=False):
    res = preco + (preco * taxa / 100)
    return res if form is False else moeda(res)


def diminuir(preco=0, taxa=0, form=False):
    res = preco - (preco * taxa / 100)
    return res if form is False else moeda(res)


def dobro(preco=0, form=False):
    res = preco * 2
    return res if form is False else moeda(res)


def metade(preco=0, form=False):
    res = preco / 2
    return res if form is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxaMais=0, taxaMenos=0):
    divs = 30 * "-"
    print(f'{divs}'
          f'\n{"RESUMO DO VALOR":^30}'
          f'\n{divs}'
          f'\nPreço Analisado: \t{moeda(preco)}'
          f'\nDobro do Preço: \t{dobro(preco, True)}'
          f'\nMetade do Preço: \t{metade(preco, True)}'
          f'\n{taxaMais}% de aumento: \t{aumentar(preco, taxaMais, True)}'
          f'\n{taxaMenos}% de redução: \t{diminuir(preco, taxaMenos, True)}'
          f'\n{divs}')