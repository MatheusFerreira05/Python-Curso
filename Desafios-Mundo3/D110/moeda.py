def metade(n,f=False):
    if f == True:
        return moeda(n/2)
    else:
        return n / 2

def dobro(n,f=False):
    if f == True:
        return moeda(n*2)
    else:
        return n*2

def aumentar(n, p,f=False):
    if f == True:
        return moeda(n + (n * (p/100)))
    else:
        return n + (n * (p/100))

def diminuir(n,p,f=False): 
    if f == True:
        return moeda(n - (n * (p/100)))
    else:
        return n - (n * (p/100))

def moeda(n):
    return f'R${n:.2f}'.replace('.',',')

def resumo(n, a, r):
    print('-'*30)
    print('RESUMO DO VALOR')
    print('-'*30)
    print(f'Preço analisado: {moeda(n)}')
    print(f'Dobro do preço: {dobro(n,True)}')
    print(f'Metade do preço: R${metade(n,True)}')
    print(f'{a}% de aumento: R${aumentar(n,a,True)}')
    print(f'{r}% de redução: {diminuir(n,r,True)}')
    print('-'*30)