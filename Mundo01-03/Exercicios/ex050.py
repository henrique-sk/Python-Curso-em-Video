soma = 0
cont = 0
for i in range(1, 7):
    numeros = int(input('Digite o {}° número inteiro: '.format(i)))
    if numeros % 2 == 0:
        soma += numeros
        cont += 1
print('Existem {} números pares e '
      'a soma dos números pares é igual a {}.'.format(cont, soma))
