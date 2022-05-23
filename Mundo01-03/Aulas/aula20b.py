def contador(* núm):
    print(f'A tupla gerada é {núm}.'
          f'\nPossui {len(núm)} números.'
          f'\nOs valores são:', end='')
    for valor in núm:
        print(f' {valor}', end='')
    print(f'.\n{45*"-"}')


contador(2, 5, 56, 3)
contador(2, 5, 56, 3, 4, 2, 10)
