km_Rodados = float(input('Escreva a quantidade de km rodados com o carro: '))
qtd_dias = float(input('Escreva a quantidade de dias que ficou com o carro: '))

valorKm = km_Rodados * 0.15
valorQtdDias = qtd_dias * 60

valorTotal = valorKm + valorQtdDias

print('O valor total ficou: R$ {:.2f}'.format(valorTotal))
print('=============================')
print('===Detalhamento de valor:====')
print('Quantidade de KM: {}'.format(km_Rodados))
print('Valor KM: R$ 0.15')
print('Valor total por KM rodado: {}'.format(valorKm))
print('Quantidade de Dias: {}'.format(qtd_dias))
print('Valor KM: R$ 60')
print('Valor total por Dia de Aluguel: {:.2f}'.format(valorQtdDias))