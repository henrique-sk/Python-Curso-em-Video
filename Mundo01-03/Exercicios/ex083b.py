pilha = []
expressao = input('Digite a expressão: ')
for parenteses in expressao:
    if parenteses == '(':
        pilha.append('(')
    elif parenteses == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
