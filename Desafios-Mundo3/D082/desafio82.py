valores = []
impar = []
par = []
while True:
    valor = int(input('Digte um valor: '))
    valores.append(valor)

    if valor % 2==0:
        par.append(valor)
    else:
        impar.append(valor)

    if input('Quer continuar? [S/N]: ').upper() == 'N':
        break
print(f'A lista completa é {valores}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')