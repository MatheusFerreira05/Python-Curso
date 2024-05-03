jogador = {}
jogadores = []

while True:
    jogador['nome'] = input('Nome do jogador: ')
    gols = []
    totGol = 0
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for c in range (1,partidas+1):
        
        numGols = int(input(f'Quantos gols na partida {c}? '))
        gols.append(numGols)

    jogador['gols'] = gols[:]

    for gol in gols:
        totGol += gol
    jogador['total'] = totGol

    jogadores.append(jogador.copy())

    cont = input('Deseja continuar? [S/N]: ')

    if cont in 'Nn':
        break

print('-='*30)
print(f'{"nº":<4}{"Nome":<10}{"Gols":>8}{"Total":>12}')
print('-'*60)
for i,joga in enumerate(jogadores):
    print(f'{i+1:<4}',end=' ')
    print(f'{joga["nome"]}',end='        ')
    print(f'{joga["gols"]}',end='        ')
    print(f'{joga["total"]}')

consulta = int(input('Qual jogador você quer ver as estatísticas? '))
while consulta-1 >= len(jogadores):
    print(f'Erro! Não existe jogador com código {consulta}')
    consulta = int(input('Qual jogador você quer ver as estatísticas? '))
print(jogadores[consulta-1])



