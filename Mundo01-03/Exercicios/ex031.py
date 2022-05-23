d = int(input('Quantos Km você vai percorrer no trajeto da sua viagem? '))
frase = 'Sua passagem vai custar'
if d <= 200:
    p = d * .5
else:
    p = d * .45
print(frase, 'R${:.2f}.'.format(p))

# OU
# d = int(input('Quantos Km você vai percorrer no trajeto da sua viagem? '))
# frase = 'Sua passagem vai custar'
# p = d * .5 if d <= 200 else d * .45
# print(frase, 'R${:.2f}.'.format(p))
