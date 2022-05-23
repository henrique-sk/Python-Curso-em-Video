from random import randint as ri
from time import sleep

print(30 * '-')
print(f'{"JOGA NA MEGA SENA":^30}')
print(30 * '-')
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
num = []
lista = []
aleatorio = ri(1, 61)
for i in range(0, jogos):
    for n in range(0, 6):
        while aleatorio in num:
            aleatorio = ri(1, 61)
        num.append(aleatorio)
    lista.append(num[:])
    num.clear()
print(3 * '-=', f' SORTEANDO {jogos} JOGOS ', 3 * '-=')
for chave, valor in enumerate(lista):
    print(f'Jogo {chave+1}: {sorted(lista[chave])}')
    sleep(0.5)
print(5*'-=', f'< BOA SORTE! >', 5*'-=')
