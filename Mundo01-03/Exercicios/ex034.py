sal = float(input('Digite o seu salário R$'))
if sal <= 1250:
    aum = sal * 1.15
else:
    aum = sal * 1.1
print('Após o aumento, seu salário será R${:.2f}.'.format(aum))