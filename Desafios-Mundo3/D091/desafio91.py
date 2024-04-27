from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}
ranking = list()

for c in range(1,5):
    numero = randint(1,6)
    jogadores[f'jogador {c}'] = numero
print('-='*30)
print('== NÚMEROS SORTEADOS ==')
for c,j in jogadores.items():
    print(f'O {c} tirou {j}')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('-='*30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')



