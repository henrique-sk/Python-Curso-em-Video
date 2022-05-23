total18 = men = women = 0
while True:
    sex = continuE = ' '
    header = 'CADASTRE UMA PESSOA'
    print(30 * '-')
    print(f'{header:^30}')
    print(30 * '-')
    age = int(input('Idade: '))
    while sex not in 'MF':
        sex = input('Sexo: [M/F] ').strip().upper()[0]\
            .replace(' ', '')
    if age > 18:
        total18 += 1
    if sex == 'M':
        men += 1
    if age < 20 and sex == 'F':
        women += 1
    print(30 * '-')
    while continuE not in 'SN':
        continuE = input('Quer continuar? [S/N] ').strip()\
            .upper()[0].replace(' ', '')
    if continuE == 'N':
        break
print(6 * '=', ' FIM DO PROGRAMA ', 6 * '=')
print(f'Total de pessoas com mais de 18 anos: {total18}.'
      f'\nAo todo temos {men} homens cadastrados.'
      f'\nE temos {women} mulheres com menos de 20 anos.')
