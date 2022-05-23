from datetime import date

ano = int(input('Jovem! Em que ano você nasceu? '))
idade = date.today().year - ano
diferenca = abs(idade - 18)
if idade < 18:
    print('Você completa {} anos esse ano.'
          '\nAinda falta {} ano(s) para você se alistar.'.format(idade, diferenca))
elif idade == 18:
    print('Você completa {} anos esse ano.'
          '\nDeve se alistar já!!!'.format(idade))
else:
    print('Você completa {} anos esse ano.'
          '\nDevia ter se alistado a {} ano(s)!!!'.format(idade, diferenca))
