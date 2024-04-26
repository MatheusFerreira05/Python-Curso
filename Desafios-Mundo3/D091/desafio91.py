from random import randint

jogadores = {}
maior = 0
for c in range(1,5):
    numero = randint(1,6)
    jogadores[f'jogador{c}'] = numero

for c,j in jogadores.items():
    print(f'O {c} tirou {j}')

print('Ranking dos jogadores: ')



