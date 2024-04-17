soma = 0
for num in range(1,7):
    numero = int(input('Digite o {} número: '.format(num)))
    if numero % 2 == 0:
        soma += numero
print('A soma dos números pares digitados é igual a {}'.format(soma))