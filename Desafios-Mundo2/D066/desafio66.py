
num = soma = qtd = 0
while True:
    num = int(input('Digite um número inteiro: '))
    if num != 999:
        soma += num
        qtd += 1
    else:
        break
print(f'A soma dos {qtd} valores é {soma}')