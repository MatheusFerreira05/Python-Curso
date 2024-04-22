from random import choice

numeros = [1,2,3,4,5,6,7,8,9,10]

escolha = choice(numeros)

chute = int(input('Digite um número para tentar acertar: '))

tentativas = 1

while chute != escolha:
    chute = int(input('Digite um número para tentar acertar: '))
    tentativas += 1

print('Você ganhou! o Número era {}, você teve {} chutes'.format(escolha,tentativas))