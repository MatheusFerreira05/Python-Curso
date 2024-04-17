casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o salário do comprador? '))
anos = int(input('Em quantos anos ele pretende pagar? '))

meses = anos * 12
prestacao = casa / meses
porcentagem = salario * 0.30

if prestacao>porcentagem:
    print('=-'*20)
    print('Com base nas seguintes informações: ')
    print('Salário: R${}'.format(salario))
    print('Prestação: R${:.2f}'.format(prestacao))
    print('Parcela acessível: R${}'.format(porcentagem))
    print('Meses: {}'.format(meses))
    print('=-'*20)
    print('Infelizmente seu fiananciamento não foi aprovado...')
else:
    print('=-'*20)
    print('Com base nas seguintes informações: ')
    print('Salário: R${}'.format(salario))
    print('Prestação: R${:.2f}'.format(prestacao))
    print('Parcela acessível: R${}'.format(porcentagem))
    print('Meses: {}'.format(meses))
    print('=-'*20)
    print('O seu financiamento foi aprovado, Parabéns!')