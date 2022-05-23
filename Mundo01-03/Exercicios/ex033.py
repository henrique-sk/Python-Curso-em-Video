a = float(input('Digite o primeiro número: '))
b = float(input('Digite o segundo número: '))
c = float(input('Digite o terceiro número: '))
print('Os numeros digitados são: {:.2f}, {:.2f} e {:.2f}, respectivamente.'.format(a, b, c))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor é {} e o maior é {}'.format(menor, maior))
