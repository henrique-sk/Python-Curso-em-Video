lista = []
for posicao in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {posicao}: ')))
print(30 * '=-')
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for chave, valor in enumerate(lista):
    if valor == max(lista):
        print(f'{chave}... ', end='')
print(f'\nO menor valor digitado foi {min(lista)} nas posições ', end='')
for chave, valor in enumerate(lista):
    if valor == min(lista):
        print(f'{chave}... ', end='')
