from time import sleep

def contador(inicio,fim,passo):
    print('-='*25)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2)
    for num in range(inicio,fim+1,passo):
        print(num,end=' => ')
        sleep(1)
    print('FIM!')
    print('-='*25)

contador(1,10,1)

contador(10,0,-2)

print('Agora é sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
if i < f:
    if p != 0:
        contador(i,f,p)
    else:
        contador(i,f,1)
else:
    if p != 0:
        contador(i,f,-p)
    else:
        contador(i,f,-1)