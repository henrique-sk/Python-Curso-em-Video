n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
m = (n1 + n2) / 2
print(m)
if m < 5:
    print('Sua média é {:.1f}. Está REPROVADO!'.format(m))
elif 5 >= m < 7:
    print('Sua média é {:.1f}. Está em RECUPERÇÂO!'.format(m))
else:
    print('PARABÉNS!!! Sua média é {:.1f}. Está APROVADO!'.format(m))
