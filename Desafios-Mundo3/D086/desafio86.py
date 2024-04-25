matriz = [[[],[],[]],[[],[],[]],[[],[],[]]]

for c in range(0,9):
    valor = int(input(f'Digite o {c+1}º valor '))
    if c <= 2:
        matriz[0][c].append(valor)
    elif 2 < c <= 5:
        matriz[1][c-3].append(valor)
    elif 5 < c <= 8:
        matriz[2][c-6].append(valor)

print('=-'*30)
print(matriz[0])
print(matriz[1])
print(matriz[2])
