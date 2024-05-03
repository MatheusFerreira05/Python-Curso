def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato')

nome = input('Qual é o nome do jogador? ')
gols = input('Quantos gols ele fez? ')

if nome == '':
    ficha(gols=gols)
elif gols == '':
    ficha(nome=nome)
elif nome == '' and gols == '':
    ficha()
else:
    ficha(nome,gols)