from random import randint
from time import sleep


def sorteia():
    numeros = list()
    numeros.append(randint(1,10))
    numeros.append(randint(1,10))
    numeros.append(randint(1,10))
    numeros.append(randint(1,10))
    numeros.append(randint(1,10))
    print(f'Sorteando 5 valores da lista: ',end='')
    for n in numeros:
        print(n,end=' ')
        sleep(1)
    print('PRONTO!')
    return numeros

def somaPar(sorteados):
    Somapares = 0
    pares = list()
    print(f'Os valores pares foram: ',end='')
    for n in sorteados:
        if n % 2 ==0:
            Somapares += n
            pares.append(n)
            print(n,end=' ')
            sleep(1)
    print('e a soma foi: ', end='')
    print(Somapares)
    

        

lista = sorteia()

somaPar(lista)

