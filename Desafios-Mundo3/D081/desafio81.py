valores = []
qtd = 0
cincoNaLista = 0
while True:
    valor = int(input('Digte um valor: '))
    valores.append(valor)
    qtd += 1
    if valor == 5:
        cincoNaLista = 1
    if input('Quer continuar? [S/N]: ').upper() == 'N':
        break

valores.sort(reverse=True)
print(f'Foram digitados {qtd} elementos.')
print(f'Os valores em ordem decrescente são {valores}')

if cincoNaLista == 1:
    print(f'O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')