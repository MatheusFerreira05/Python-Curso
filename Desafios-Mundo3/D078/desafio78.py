valores = []
c = 0
qtd = 1
menorValor = maiorValor = int(input('Digite um valor: '))
valores.append(menorValor)
while c < 4:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    c += 1
    if menorValor >= valor:
        menorValor = valor
    if maiorValor <= valor:
        maiorValor = valor

print(f'Você digitou os seguintes valores: {valores}')
print(f'Esse é o maior valor digitado: {maiorValor} nas posições ',end='')
for i,v in enumerate(valores):
    if v == maiorValor:
        print(f'{i}...',end='')
print(f'Esse é o menor valor digitado: {menorValor} nas posições ',end='')
for i,v in enumerate(valores):
    if v == menorValor:
        print(f'{i}...',end='')
