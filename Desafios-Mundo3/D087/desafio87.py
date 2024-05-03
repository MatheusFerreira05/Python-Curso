matriz = [[[],[],[]],[[],[],[]],[[],[],[]]]
somaPar = maiorValor = somaTerceira =0
for c in range(0,9):
    valor = int(input(f'Digite o {c+1}º valor '))
    if c <= 2:
        matriz[0][c].append(valor)
    elif 2 < c <= 5:
        matriz[1][c-3].append(valor)
    elif 5 < c <= 8:
        matriz[2][c-6].append(valor)
    
    if valor %2 == 0:
        somaPar += valor

print('=-'*30)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('=-'*30)
print(f'A soma dos números pares é {somaPar}')
for l in range(0, 3):
    somaTerceira += matriz[l][2][0]
print(f'A soma da terceira coluna é {somaTerceira}')

if matriz[1][0] > matriz[1][1] and matriz[1][0] > matriz[1][2]:
    print(f'O maior valor da segunda linha é {matriz[1][0]}')
elif matriz[1][1] > matriz[1][0] and matriz[1][1] > matriz[1][2]:
    print(f'O maior valor da segunda linha é {matriz[1][1]}')
elif matriz[1][2] > matriz[1][1] and matriz[1][2] > matriz[1][0]:
    print(f'O maior valor da segunda linha é {matriz[1][2]}')
