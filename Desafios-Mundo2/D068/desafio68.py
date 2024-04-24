from random import choice
valores = [1,2,3,4,5,6,7,8,9,10]
vitorias = 0
while True:
    print('-='*35)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('-='*35)
    valorJogador = int(input('Diga um valor: '))
    parImpar = input('Par ou Ímpar? [P/I]').upper().strip()
    valorMaquina = choice(valores)
    soma = valorMaquina + valorJogador
    if soma %2 == 0 and parImpar == 'P' or soma %2 == 1 and parImpar == 'I':
        jogador = 1
        print(f'Você venceu a rodada! Você colocou {valorJogador} e a máquina {valorMaquina} somando {soma} e sua escolha foi {parImpar}')
    else:
        jogador = 2
        print(f'Você perdeu! Você colocou {valorJogador} e a máquina {valorMaquina} somando {soma} e sua escolha foi {parImpar}')
    if jogador == 1:
        vitorias += 1
    else:
        break

if vitorias > 1:
    print(f'Você ganhou {vitorias} vezes')
elif vitorias == 1:
    print(f'Você ganhou {vitorias} vez')
elif vitorias == 0:
    print(f'Você não venceu nenhuma vez')