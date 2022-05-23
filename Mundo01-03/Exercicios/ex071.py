print(30 * '=')
print('{:^30}'.format('BANCO HSK'))
print(30 * '=')
valor = int(input('Que valor você quer sacar? R$'))
total = valor
ced = 50
totCed = 0
while True:
    if total >= ced:
        totCed += 1
        total -= ced
    else:
        if totCed > 0:
            print(f'Total de {totCed} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totCed = 0
        if total == 0:
            break
print(30 * '=')
print('Volte sempre ao BANCO HSK! Tenha um bom dia!')
