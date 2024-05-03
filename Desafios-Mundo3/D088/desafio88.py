from random import randint
from time import sleep
print('=-'*15)
print('      JOGA MEGA SENA    ')
print('=-'*15)
palpites = int(input('Quantos jogos você quer gerar? '))
c = 0
while c < palpites:
    jogo = []
    for num in range(1,7):
        aleatorio = randint(1,60)
        while aleatorio in jogo:
            aleatorio = randint(1,60)
        else:
            jogo.append(aleatorio)
    c +=1
    jogo.sort()
    print(f'Jogo {c}: {jogo}')
    sleep(2)

print('-='*5 , 'BOA SORTE!' , '-='*5)
    