lista = [[], []]
for i in range(0, 7):
    valor = int(input(f'Digite o {i+1}° valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(30 * '-=')
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram {lista[0]}.')
print(f'Os valores ímpares digitados foram {lista[1]}.')
