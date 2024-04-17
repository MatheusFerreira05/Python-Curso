salario = float(input('Digite o salário bruto atual do funcionário: '))
aumento = salario * 0.15

novo_salario = salario + aumento

print('O salário de R$ {:.2f} com aumento de 15% é igual a {:.2f}'.format(salario,novo_salario))