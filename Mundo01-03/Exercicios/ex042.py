r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segundaa reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas 3 retas PODEM formar um triângulo! E é um triângulo ', end='')
    if r1 == r2 == r3:
        print('equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        # OU elif r1 != r2 != r3 != r1
        print('isóceles.')
    else:
        print('escaleno.')
else:
    print('Essas 3 retas NÃO PODEM formar um triângulo!')
