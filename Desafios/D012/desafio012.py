preco = float(input('Digite o valor total do produto: '))
desconto = preco * 0.05

preco_desconto = preco - desconto

print('O produto com valor de R$ {:.2f} com 5% de desconto é igual a {:.2f}'.format(preco,preco_desconto))