lista = []

for i in range(0, 5):
    num = int(input('Digite um valor: '))
    if i == 0 or num > lista[-1]: # OU lista[len(lista)-1]
        # testa se é o primeiro ou maior que o último
        lista.append(num)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print(30 * '-=')
print(f'Os valores digitados em ordem foram {lista}')
