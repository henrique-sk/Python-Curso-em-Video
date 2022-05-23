cont = soma = 0
num = int(input('Digite um número inteiro'
                ' [999 para parar!]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número inteiro'
                    ' [999 para parar!]: '))
print('Programa encerrado!'
      '\nForam digitados {} números. '
      'A soma entre eles é {}.'.format(cont, soma))
