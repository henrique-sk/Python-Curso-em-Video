lanche = 'Hamburger', 'Suco', 'Pizza', 'Pudim', 'Fritas'

for comida in lanche:
    print(f'Vou comer {comida}.')
print('Estou cheio!!')

for cont in range(0, len(lanche)):
    print(f'{cont} - Vou comer {lanche[cont]}.')
print('Estou cheio!!')

for pos, comida in enumerate(lanche):
    print(f'{pos} - Vou comer {comida}.')
print('Estou cheio!!')

print(sorted(lanche))
print(lanche)
