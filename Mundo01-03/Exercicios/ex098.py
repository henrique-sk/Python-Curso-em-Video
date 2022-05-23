def contador(i, f, p):
    from time import sleep as sl
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print(f'{20 * "-="}'
          f'\nContagem de {i} até {f} de {p} em {p}')
    if f > i and p > 0:
        f += 1
    elif i > f and p > 0:
        f -= 1
        p *= -1
    elif i > f:
        f -= 1
    if f < 0:
        f += 1
    for n in range(i, f, p):
        print(n, end=' ')
        sl(.1)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print(f'{20 * "-="}'
      f'\nAgora é a sua vez de personalizar a contagem!')
contador(int(input(f'{"Início: ":<8}')),
         int(input(f'{"Fim: ":<8}')),
         int(input(f'{"Passo: ":<8}')))
