jogador = {}
gols = []
totGol = 0
jogador['nome'] = input('Nome do jogador: ')

partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for c in range (1,partidas+1):
    numGols = int(input(f'Quantos gols na partida {c}? '))
    gols.append(numGols)

jogador['gols'] = gols

for gol in gols:
    totGol += gol

jogador['total'] = totGol

print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')

for c,g in enumerate(gols):
    print(f' => Na partida {c+1}, fez {g} gols.')
print(f'Foi um total de {totGol} gols.')


