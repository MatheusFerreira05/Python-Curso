def area(b,h):
    area = b * h
    print(f'A área do terreno {b}x{h} é de {area}m2')

print('Controle de Terrenos')
print('-'*30)
base = float(input('LARGURA (m): '))
altura = float(input('COMPRIMENTO (m): '))
area(base,altura)