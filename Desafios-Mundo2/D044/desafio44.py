valor = float(input('Qual o valor do produto? '))
print('''DIGITE a opção de pagamento: 
      1 - Á vista ou Dinheiro
      2 - Cartão
      3 - 2x no cartão
      4 - 3 ou mais vezes no cartão
      ''')
formaPgto = int(input('Digite a opção desejada: '))

if formaPgto == 1:
    desconto = valor * 0.10
    print('O valor total é de R${:.2f}, porém com o desconto de 10% ficou R${}'.format(valor,valor-desconto))
elif formaPgto == 2:
    desconto = valor * 0.05
    print('O valor total é de R${:.2f}, porém com o desconto de 5% ficou R${}'.format(valor,valor-desconto))
elif formaPgto == 3:
    print('O valor total é de R${:.2f}'.format(valor))
elif formaPgto == 4:
    acrescimo = valor * 0.20
    print('O valor total é de R${:.2f}, porém com juros de 20% ficou R${}'.format(valor,valor+acrescimo))