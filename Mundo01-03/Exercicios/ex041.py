from datetime import date

ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
if idade <= 9:
    print('Você tem {} anos. Sua categoria é MIRIM!'.format(idade))
elif idade <= 14:
    print('Você tem {} anos. Sua categoria é INFANTIL!'.format(idade))
elif idade <= 19:
    print('Você tem {} anos. Sua categoria é JUNIOR!'.format(idade))
elif idade <= 25:
    print('Você tem {} anos. Sua categoria é SÊNIOR!'.format(idade))
else:
    print('Você tem {} anos. Sua categoria é MASTER!'.format(idade))
