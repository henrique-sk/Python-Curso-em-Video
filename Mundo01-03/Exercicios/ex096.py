def area(l, c):
    a = l * c
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {a:.1f}m².')


print(f'Controle de Terrenos'
      f'\n{20*"-"}')
area(float(input('LARGURA(m): ')), float(input('COMPRIMENTO(m): ')))
