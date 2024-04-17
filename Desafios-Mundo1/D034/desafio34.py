salario = float(input('Digite o valor do salário do funcionário: R$ '))

if salario > 1250.00:
    aumento = (salario * 0.10) + salario
    print('O salário é superior a R$ 1250,00, portanto o aumento é de 10% ficando R${:.2f}'.format(aumento))
else:
    aumento = (salario * 0.15) + salario
    print('O salário é inferior a R$ 1250,00, portanto o aumento é de 15% ficando R${:.2f}'.format(aumento))