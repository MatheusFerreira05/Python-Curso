distancia = int(input('Digite a distância da viagem em KM: '))

if distancia <= 200:
    valor = distancia * 0.50
    print('Sua viagem é de {} km portanto cobraremos R$ 0,50 por km então o valor da sua passagem é de R$ {:.2f}'.format(distancia,valor))
else:
    valor = distancia * 0.45
    print('Sua viagem é de {} km portanto cobraremos R$ 0,45 por km então o valor da sua passagem é de R$ {:.2f}'.format(distancia,valor))