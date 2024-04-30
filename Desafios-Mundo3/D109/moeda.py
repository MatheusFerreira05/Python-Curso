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