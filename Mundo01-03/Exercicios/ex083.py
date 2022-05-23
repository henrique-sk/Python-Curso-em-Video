pilha = []
expressao = input('Digite a expressão: ')
for i in expressao:
    pilha.append(i)
cont1 = cont2 = 0
for valor in pilha:
    if valor == '(':
        cont1 += 1
    elif valor == ')':
        cont2 += 1
if cont1 == cont2:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
