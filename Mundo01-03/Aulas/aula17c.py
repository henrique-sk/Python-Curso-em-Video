a = [2, 3, 4, 7]
print(a)
b = a # isso não copia a lista, cria uma ligação
b[2] = 8 # isso muda nas duas
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#para crias CÓPIA dos valores
a2 = [2, 3, 4, 7]
b2 = a2[:] # assim, b recebe todos itens de a (fatiamento)
b2[2] = 8
print(f'Lista A: {a2}')
print(f'Lista B: {b2}')
