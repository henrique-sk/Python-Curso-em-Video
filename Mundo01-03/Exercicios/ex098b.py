def contador(i, f, p):
    from time import sleep as sl
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print(f'{20 * "-="}'
          f'\nContagem de {i} até {f} de {p} em {p}')
    if f > i:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sl(.1)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sl(.1)
            cont -= p
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print(f'{20 * "-="}'
      f'\nAgora é a sua vez de personalizar a contagem!')
contador(int(input(f'{"Início: ":<8}')),
         int(input(f'{"Fim: ":<8}')),
         int(input(f'{"Passo: ":<8}')))
