print('='*30)
print('BANCO MATHEUS')
print('='*30)
valor = int(input('Qual valor você quer sacar? R$'))
total = valor
cedulas = 50
totalCedulas = 0

while True:
    if total >= cedulas:
        total -= cedulas
        totalCedulas += 1
    else:
        if totalCedulas > 0:
            print(f'Total de {totalCedulas} cédulas de R${cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        totalCedulas = 0
        if total == 0:
            break

print('='*30)
print('Volte sempre ao Banco do Matheus')