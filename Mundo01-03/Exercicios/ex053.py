frase = input('Digite uma frase: ').upper()
junto = frase.replace(' ', '')
# palavras = frase.split()  # uma alternativa
# junto = ''.join(palavras) # ao replace()
inverso = junto[::-1]
# inverso = '' # junto[::-1] substitui o for
# for letra in range(len(junto) - 1, -1, -1):
#     inverso += junto[letra]
print('A frase digitada é {} e seu inverso é {}.'.format(junto, inverso))
if junto == inverso:
    print('Temos um palíndromo!!')
else:
    print('Não é um palíndromo.')
