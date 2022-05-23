from random import randint as ri
from time import sleep as sl
from operator import itemgetter as ig

jogo = {}
for c in range(0, 4):
    jogo[f'jogador{c+1}'] = ri(1, 6)
ranking = []
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sl(.5)
ranking = sorted(jogo.items(), key=ig(1), reverse=True)
print(f'{"-="*30}\n== RANKING DOS JOGADORES ==')
for index, value in enumerate(ranking):
    print(f'   {index}° lugar: {value[0]} com {value[1]}.')
    sl(.5)
