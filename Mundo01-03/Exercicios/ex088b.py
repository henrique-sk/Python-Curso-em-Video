from random import randint as ri
from time import sleep

lista = []
jogos = []
print(30 * '-')
print(f'{"JOGA NA MEGA SENA":^30}')
print(30 * '-')
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        aleatorio = ri(1, 61)
        if aleatorio not in lista:
            lista.append(aleatorio)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(3 * '-=', f' SORTEANDO {quant} JOGOS ', 3 * '-=')
for chave, valor in enumerate(jogos):
    print(f'Jogo {chave+1}: {valor}')
    sleep(0.5)
print(5*'-=', f'< BOA SORTE! >', 5*'-=')
