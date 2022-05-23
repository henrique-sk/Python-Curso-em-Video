palavras = 'aprender', 'programar', 'linguagem', 'python',\
           'curso', 'gratis', 'estudar', 'praticar',\
           'trabalhar', 'mercado', 'programador', 'futuro'
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if (letra.lower()) in 'aeiou':
            print(letra, end=' ')

#vogais = 'aeiou'
# for p in range(len(palavras)):
#     print(f'\nNa palavra {palavras[p].upper()} temos ', end='')
#     for i in range(len(palavras[p])):
#         for c in range(len(vogais)):
#             if (vogais[c].find(palavras[p][i].lower())) == 0:
#                 print(palavras[p][i], end=' ')
