elementos = int(input('Quantos elementos da '
                      'sequência de Fibonacci '
                      'você deseja ver? '))
c = 1
n1 = 0
n2 = 0
while c < elementos:
    if n2 < 1:
        print(n2, end=' ')
        n2 = 1
        print(n2, end=' ')
        c += 1
    else:
        soma = n1 + n2
        n1 = n2
        n2 = soma
        c += 1
        print(n2, end=' ')
