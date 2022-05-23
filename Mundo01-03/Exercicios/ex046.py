from time import sleep
from emoji import emojize

fogos = emojize(10 * ':fireworks:', language='alias')
print('Prepare-se para o estouro dos fogos!!!')
for i in range(10, -1, -1):
    print(i)
    sleep(0.5)
print(fogos)
sleep(0.5)
print(fogos)
sleep(0.2)
print(fogos)
sleep(0.6)
print(fogos)
