from random import choice

numeros = [1,2,3,4,5]

escolha = choice(numeros)

chute = int(input('Digite um número para tentar acertar: '))

if chute == escolha:
    print('Parabéns! Você acertou!')
else:
    print('Você errou! o número era {}'.format(escolha))