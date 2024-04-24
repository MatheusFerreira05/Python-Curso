valores = []
while True:
    valor = int(input('Digte um valor: '))
    
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor já adicionado anteriomente! ')
    
    if input('Quer continuar? [S/N]: ').upper() == 'N':
        break

valores.sort()
print(f'Os valores adicionados foram: {valores}')
