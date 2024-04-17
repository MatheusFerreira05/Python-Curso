soma = 0
for impar in range(1,500):
    if impar % 2 == 1 and impar%3 == 0:
        soma += impar
print('A soma dos valores ímpares multiplos de três é igual a {}'.format(soma))