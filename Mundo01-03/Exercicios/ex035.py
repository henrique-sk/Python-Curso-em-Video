r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segundaa reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
c1 = abs(r1 - r3) < r1 < r2 + r3
c2 = abs(r1 - r3) < r2 < r1 + r3
c3 = abs(r1 - r2) < r3 < r1 + r2
if c1 and c2 and c3:
    print('Essas 3 retas podem formar um triângulo!')
else:
    print('Essas 3 retas NÃO podem formar um triângulo!')

# OU
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segundaa reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Essas 3 retas PODEM formar um triângulo!')
else:
    print('Essas 3 retas NÃO PODEM formar um triângulo!')
