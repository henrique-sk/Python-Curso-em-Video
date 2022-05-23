maior = 0
menor = 0
for c in range(1, 5):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('{:.2f}kg foi o maior peso digitado e '
      '{:.2f}kg foi o menor.'.format(maior, menor))
