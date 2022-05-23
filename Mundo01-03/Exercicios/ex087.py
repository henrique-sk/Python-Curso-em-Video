matriz = [[], [], []]
par = soma = maior = 0
for i in range(0, 3):
    for c in range(0, 3):
        matriz[i].append(int(input(f'Digite um valor para [{i}, {c}]: ')))
        if matriz[i][c] % 2 == 0:
            par += matriz[i][c]
        if c == 2:
            soma += matriz[i][2]
        if i == 1:
            if c == 0:
                maior = matriz[1][c]
            elif matriz[1][c] > maior:
                maior = matriz[1][c]
print(30 * '-=')
for i in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[i][c]:^5}]', end='')
    print(end='\n')
print(30 * '-=')
print(f'A soma dos valores pares é {par}.'
      f'\nA soma dos valores da terceira coluna é {soma}.'
      f'\nO maior valor da segunda linha é {maior}.')
