from random import choice

print('''ESCOLHA UMA OPÇÃO PARA COMEÇAR O JOKENPO

 - PEDRA
 - PAPEL
 - TESOURA
''')

opcao = input('OPÇÃO: ').upper()

possibilidades = ['PEDRA','PAPEL','TESOURA']
maquina = choice(possibilidades)

if opcao == maquina:
    print('=-'*21)
    print('Empate, ambos colocaram {}'.format(opcao))
    print('=-'*21)
elif opcao == 'TESOURA' and maquina == 'PAPEL' or opcao == 'PAPEL' and maquina == 'PEDRA' or opcao == 'PEDRA' and maquina == 'TESOURA':
    print('=-'*21)
    print('Você Venceu! Você colocou {} e a máquina escolheu {}'.format(opcao,maquina))
    print('=-'*21)
elif maquina == 'TESOURA' and opcao == 'PAPEL' or maquina == 'PAPEL' and opcao == 'PEDRA' or maquina == 'PEDRA' and opcao == 'TESOURA':
    print('=-'*21)
    print('Você perdeu... Você colocou {} e a máquina colocou {}'.format(opcao,maquina))
    print('=-'*21)

