from datetime import date

menores = 0
maiores = 0
for i in range(0, 4):
    ano = int(input('Digite o {}° ano de nascimento: '.format(i)))
    if date.today().year - ano >= 21:
        maiores += 1
    else:
        menores += 1
print('{} pessoas já são maiores de idade e'
      ' {} ainda são menores.'.format(maiores, menores))
