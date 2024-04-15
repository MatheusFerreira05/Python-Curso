carteira = int(input('Qual valor que tem em carteira: R$'))

#Considerando dólar = R$ 3.27
dolar = 3.27

qtd_dolares = carteira/dolar

print('Com R${:.2f}, você pode comprar ${:.2f}'.format(carteira,qtd_dolares))