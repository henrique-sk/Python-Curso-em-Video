# ano = int(input('Informe um ano qualquer: '))
# bi = 'O ano É bissexto!'
# nbi = 'O ano NÃO é bissexto!'
# if ano % 4 == 0:
#     if ano % 100 == 0:
#         if ano % 400 == 0:
#             print(bi)
#         else:
#             print(nbi)
#     else:
#         print(bi)
# else:
#     print(nbi)

# OU
from datetime import date

ano = int(input('Informe um ano qualquer. Use "0" se quiser analisar o ano atual: '))
bi = 'O ano {} É bissexto!'
nbi = 'O ano {} NÃO é bissexto!'
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(bi.format(ano))
else:
    print(nbi.format(ano))
